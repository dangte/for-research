#!/usr/bin/env python3
"""Validate every SKILL.md: must have YAML frontmatter with non-empty name + description."""
import sys
import pathlib

try:
    import yaml
except ImportError:
    print("PyYAML not installed", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parents[2]
errors = []
checked = 0

for path in sorted(ROOT.rglob("SKILL.md")):
    checked += 1
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{rel}: missing YAML frontmatter (no leading '---')")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{rel}: frontmatter not closed with '---'")
        continue
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        errors.append(f"{rel}: invalid YAML frontmatter ({e})")
        continue
    if not isinstance(meta, dict):
        errors.append(f"{rel}: frontmatter is not a mapping")
        continue
    for key in ("name", "description"):
        val = meta.get(key)
        if not (isinstance(val, str) and val.strip()):
            errors.append(f"{rel}: missing or empty '{key}'")

print(f"Checked {checked} SKILL.md file(s).")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("All SKILL.md files valid.")
