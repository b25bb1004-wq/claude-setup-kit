"""Static tests for the kit. Run with `python -m pytest bench/test_static.py` or plain `python bench/test_static.py`.

Costs nothing: no model calls. The installer tests write only to temporary folders.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
PY = sys.executable

# Shell builtins and basic coreutils that every supported shell has; anything else a skill
# runs must be named in requirements.md.
BASE_COMMANDS = set("""
bash sh cd echo export set unset for until while if exec kill sleep timeout which chmod cp mv rm ls head
tail wc du tr sed grep cmp free cat find mkdir touch printf env source test
""".split())
# Backticked words that look like commands but are config keys, flags or prose in the skills.
NOT_COMMANDS = set("""
chat_template_kwargs chunk_gated_delta_rule max_model_len mv1 n-cpu-moe ngl fa tok model stage listen span.word mcp
""".split())


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def test_validator_passes():
    r = run([PY, str(REPO / "scripts" / "validate_skills.py")])
    assert r.returncode == 0, r.stdout + r.stderr


def test_sanitizer_passes():
    # Uses the private term list too when SANITIZE_TERMS is set.
    r = run([PY, str(REPO / "scripts" / "sanitize.py")])
    assert r.returncode == 0, r.stdout


def _install_checks(run_install):
    with tempfile.TemporaryDirectory() as tmp:
        target = pathlib.Path(tmp) / ".claude"
        (target / "skills" / "quality-loop").mkdir(parents=True)
        (target / "CLAUDE.md").write_text("mine", encoding="utf-8")
        out = run_install(target, dry=True)
        assert "DRY RUN" in out and not (target / "settings.example.json").exists()
        out = run_install(target, dry=False)
        assert "skip (exists)" in out
        assert (target / "CLAUDE.md").read_text(encoding="utf-8") == "mine"
        assert not any((target / "skills" / "quality-loop").iterdir())
        shipped = {p.name for p in SKILLS.iterdir() if p.is_dir()}
        assert shipped <= {p.name for p in (target / "skills").iterdir()}
        assert "0 copied" in run_install(target, dry=False)


def test_install_sh():
    bash = shutil.which("bash")
    if not bash:
        return  # shortcut: skipped where bash is missing; Windows CI should use Git Bash

    def go(target, dry):
        env = dict(os.environ, CLAUDE_HOME=str(target))
        r = run([bash, str(REPO / "scripts" / "install.sh")] + (["--dry-run"] if dry else []), env=env)
        assert r.returncode == 0, r.stderr
        return r.stdout

    _install_checks(go)


def test_install_ps1():
    ps = shutil.which("pwsh") or shutil.which("powershell")
    if not ps:
        return  # shortcut: skipped where PowerShell is missing

    def go(target, dry):
        cmd = [ps, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(REPO / "scripts" / "install.ps1"),
               "-Target", str(target)] + (["-DryRun"] if dry else [])
        r = run(cmd)
        assert r.returncode == 0, r.stderr
        return r.stdout

    _install_checks(go)


def _dropped_names():
    text = (REPO / "DROPPED.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\| ([a-z0-9-]+) \|", text, flags=re.M))


def test_skills_reference_only_shipped_things():
    shipped = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    dropped = _dropped_names() - shipped
    problems = []
    for f in sorted(SKILLS.glob("*/SKILL.md")):
        text = f.read_text(encoding="utf-8")
        for span in re.findall(r"`([^`\n]+)`", text):
            if span in dropped:
                problems.append(f"{f.parent.name}: refers to dropped skill {span}")
            for m in re.findall(r"(?<![\w/.~])skills/([a-z0-9-]+)", span):
                if m not in shipped:
                    problems.append(f"{f.parent.name}: refers to missing skills/{m}")
        # files that ship with a skill must exist next to it
        for m in re.findall(r"`([\w-]+\.(?:swift|py|sh|ps1))`", text):
            if (f.parent / m).exists() or m in ("pdl.py", "gen.py", "validate.py", "x.py", "job.sh", "x.sh", "X.sh"):
                continue  # example names of files the user writes are allowed
            problems.append(f"{f.parent.name}: refers to {m}, not in the skill folder")
    assert not problems, "\n".join(problems)


def test_skill_commands_are_in_requirements():
    req = (REPO / "requirements.md").read_text(encoding="utf-8").lower()
    known = BASE_COMMANDS | set(re.findall(r"[a-z][a-z0-9._-]+", req))
    problems = []
    for f in sorted(SKILLS.glob("*/SKILL.md")):
        for span in re.findall(r"`([^`\n]+)`", f.read_text(encoding="utf-8")):
            words = span.strip().split()
            if len(words) < 2 or not re.fullmatch(r"[a-z][a-z0-9._-]+", words[0]):
                continue
            cmd = words[0]
            if cmd in NOT_COMMANDS or cmd in known:
                continue
            problems.append(f"{f.parent.name}: `{cmd}` is not listed in requirements.md")
    assert not problems, "\n".join(sorted(set(problems)))


def test_bench_parser_and_grader():
    sys.path.insert(0, str(REPO / "bench"))
    import run_bench
    stream = "\n".join([
        '{"type":"system","subtype":"init"}',
        '{"type":"assistant","message":{"content":[{"type":"tool_use","name":"Skill","input":{"skill":"quality-loop"}}]}}',
        'not json',
        '{"type":"result","result":"391","total_cost_usd":0.01,"usage":{"input_tokens":5}}',
    ])
    skills, res, _ = run_bench.parse_stream(stream)
    assert skills == ["quality-loop"] and res["result"] == "391"
    assert run_bench.grade({"type": "regex", "value": r"^\s*391\s*$"}, "391") is True
    assert run_bench.grade(None, "x") is None


if __name__ == "__main__":
    failed = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except AssertionError as e:
                failed += 1
                print("FAIL", name, "\n ", str(e)[:2000])
    sys.exit(1 if failed else 0)
