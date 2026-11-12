"""Skill-trigger benchmark: the kit installed vs a vanilla Claude Code config.

Each prompt runs headless (`claude -p`) once per config, each config in its own isolated
CLAUDE_CONFIG_DIR. It records which skills fired, whether the answer passes the prompt's
grader, wall time, tokens and cost, then writes runs.jsonl and report.md.

This spends real usage. Start with --limit 2.

Usage:
  python bench/run_bench.py --out bench/results/<name> [--limit N] [--ids p01,n01]
         [--configs kit,vanilla] [--model haiku] [--auth-file PATH] [--workdir DIR]

Auth: an isolated config dir has no login. Either set ANTHROPIC_API_KEY or
CLAUDE_CODE_OAUTH_TOKEN (from `claude setup-token`) in the environment, or pass
--auth-file pointing at your own credentials file; it is copied into each temporary config
dir for the run and deleted afterwards. It is never written to the results.
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

REPO = pathlib.Path(__file__).resolve().parent.parent


def load_prompts(limit, ids):
    rows = [json.loads(l) for l in (REPO / "bench" / "prompts.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    if ids:
        rows = [r for r in rows if r["id"] in ids]
    return rows[:limit] if limit else rows


def make_config(root, name, auth_file):
    cfg = root / name
    cfg.mkdir(parents=True)
    if name == "kit":
        env = dict(os.environ, CLAUDE_HOME=str(cfg))
        # which() follows PATH; a bare "bash" on Windows can resolve to the WSL launcher in System32
        r = subprocess.run([shutil.which("bash") or "bash", str(REPO / "scripts" / "install.sh")], env=env, capture_output=True, text=True)
        if r.returncode:
            sys.exit("kit install failed: " + r.stderr)
    if auth_file:
        shutil.copyfile(auth_file, cfg / ".credentials.json")
    return cfg


def parse_stream(stdout):
    """Return (skills fired in order, final result object or {}, skills available per the init event)."""
    skills, result, available = [], {}, None
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(ev, dict):
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            available = len(ev.get("skills") or ev.get("slash_commands") or [])
        elif ev.get("type") == "assistant":
            for block in ev.get("message", {}).get("content", []) or []:
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    skills.append(str(block.get("input", {}).get("skill", "")).split(":")[-1])
        elif ev.get("type") == "result":
            result = ev
    return skills, result, available


def grade(grader, text):
    if not grader:
        return None
    if grader["type"] == "regex":
        return re.search(grader["value"], text or "", flags=re.M) is not None
    raise ValueError(grader["type"])


def run_one(prompt, cfg, workdir, model, timeout):
    env = dict(os.environ, CLAUDE_CONFIG_DIR=str(cfg))
    # which() also finds claude.cmd on Windows
    cmd = [shutil.which("claude") or "claude", "-p", "--output-format", "stream-json", "--verbose",
           "--no-session-persistence", "--max-turns", "4", "--model", model,
           "--allowedTools", "Skill,Read,Glob,Grep"]
    # prompt goes in on stdin: claude.cmd on Windows mangles quotes and backticks in arguments
    t0 = time.time()
    try:
        r = subprocess.run(cmd, env=env, cwd=workdir, input=prompt["prompt"], capture_output=True, text=True, encoding="utf-8", timeout=timeout)
        out, err, code = r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        out, err, code = "", "timeout", -1
    wall = time.time() - t0
    skills, res, available = parse_stream(out)
    usage = res.get("usage", {}) or {}
    text = res.get("result", "")
    expected = prompt["expect_skill"]
    trigger_ok = (skills[:1] == [expected]) if expected else (not skills)
    return {
        "id": prompt["id"], "expect_skill": expected, "skills_available": available, "skills_fired": skills, "trigger_ok": trigger_ok,
        "graded": grade(prompt.get("grader"), text), "exit_code": code, "is_error": res.get("is_error", code != 0),
        "wall_s": round(wall, 1), "duration_ms": res.get("duration_ms"), "num_turns": res.get("num_turns"),
        "cost_usd": res.get("total_cost_usd"),
        "tokens": {k: usage.get(k, 0) for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")},
        "answer_head": (text or "")[:300], "stderr_head": (err or "")[:300],
    }


def report(rows, configs):
    lines = ["# Skill-trigger benchmark report", "",
             "| Config | Runs | Errors | Trigger accuracy | False fires (expected none) | Graded success | Mean wall s | Tokens (in+out+cache) | Cost USD |",
             "|---|---|---|---|---|---|---|---|---|"]
    for c in configs:
        rs = [r for r in rows if r["config"] == c]
        if not rs:
            continue
        exp_none = [r for r in rs if not r["expect_skill"]]
        graded = [r for r in rs if r["graded"] is not None]
        toks = sum(sum(r["tokens"].values()) for r in rs)
        cost = sum(r["cost_usd"] or 0 for r in rs)
        lines.append(
            f"| {c} | {len(rs)} | {sum(1 for r in rs if r['is_error'])} | "
            f"{sum(r['trigger_ok'] for r in rs)}/{len(rs)} | "
            f"{sum(1 for r in exp_none if r['skills_fired'])}/{len(exp_none)} | "
            f"{sum(1 for r in graded if r['graded'])}/{len(graded)} | "
            f"{sum(r['wall_s'] for r in rs) / len(rs):.1f} | {toks} | {cost:.4f} |")
    lines += ["", "| Config | Prompt | Expected | Fired | Trigger OK | Graded |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['config']} | {r['id']} | {r['expect_skill'] or '(none)'} | {', '.join(r['skills_fired']) or '(none)'} | {r['trigger_ok']} | {r['graded']} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--ids", default="")
    ap.add_argument("--configs", default="kit,vanilla")
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--auth-file", default="")
    ap.add_argument("--workdir", default="", help="empty folder to run in; no CLAUDE.md or AGENTS.md should sit above it")
    ap.add_argument("--timeout", type=int, default=300)
    a = ap.parse_args()

    prompts = load_prompts(a.limit, set(filter(None, a.ids.split(","))))
    configs = a.configs.split(",")
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    with tempfile.TemporaryDirectory(prefix="kitbench-") as tmp:
        root = pathlib.Path(tmp)
        workdir = pathlib.Path(a.workdir) if a.workdir else root / "work"
        workdir.mkdir(parents=True, exist_ok=True)
        try:
            cfgs = {c: make_config(root, c, a.auth_file) for c in configs}
            for p in prompts:
                for c in configs:
                    row = dict(run_one(p, cfgs[c], workdir, a.model, a.timeout), config=c, model=a.model)
                    rows.append(row)
                    print(c, p["id"], "fired:", row["skills_fired"] or "-", "trigger_ok:", row["trigger_ok"], "graded:", row["graded"], f"{row['wall_s']}s", flush=True)
        finally:
            for c in configs:  # never leave a copied credentials file behind
                cred = root / c / ".credentials.json"
                if cred.exists():
                    cred.unlink()
    (out / "runs.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    (out / "report.md").write_text(report(rows, configs), encoding="utf-8")
    print("wrote", out / "report.md")


if __name__ == "__main__":
    main()
