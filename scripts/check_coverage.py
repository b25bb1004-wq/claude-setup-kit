"""Check that every folder in a source skills dir is either shipped in skills/ or named in DROPPED.md.

Usage: python scripts/check_coverage.py <source_skills_dir>
Only folder names are read from the source; no file contents.
"""
import os
import pathlib
import re
import sys

repo = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]).expanduser()
shipped = {p.name for p in (repo / "skills").iterdir() if p.is_dir()}
dropped_text = (repo / "DROPPED.md").read_text(encoding="utf-8")
listed = set(re.findall(r"^\| ([a-z0-9-]+) \|", dropped_text, flags=re.M))
# Names that would reveal private projects are kept in a list outside the repo.
withheld_file = os.environ.get("COVERAGE_WITHHELD")
if withheld_file:
    listed |= {l.strip() for l in pathlib.Path(withheld_file).read_text(encoding="utf-8").splitlines() if l.strip()}
missing = sorted(p.name for p in src.iterdir() if p.is_dir() and not p.name.startswith(".") and p.name not in shipped and p.name not in listed)
for m in missing:
    print("NOT COVERED", m)
print(f"{len(shipped)} shipped, {len(listed)} listed in DROPPED.md, {len(missing)} not covered")
sys.exit(1 if missing else 0)
