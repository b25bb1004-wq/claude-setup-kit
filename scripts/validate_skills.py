"""Check every skills/<name>/SKILL.md has frontmatter with name (matching the folder) and description.

Usage: python scripts/validate_skills.py [skills_dir]
Exit code 1 on any problem.
"""
import pathlib
import sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "skills")
problems = []
count = 0
for d in sorted(p for p in root.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        problems.append(f"{d.name}: no SKILL.md")
        continue
    count += 1
    lines = f.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        problems.append(f"{d.name}: no frontmatter")
        continue
    try:
        end = lines.index("---", 1)
    except ValueError:
        problems.append(f"{d.name}: frontmatter not closed")
        continue
    fields = {}
    for line in lines[1:end]:
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    if fields.get("name") != d.name:
        problems.append(f"{d.name}: name is {fields.get('name')!r}, expected folder name")
    if len(fields.get("description", "")) < 20:
        problems.append(f"{d.name}: description missing or too short")

for p in problems:
    print("FAIL", p)
print(f"{count} skills checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
