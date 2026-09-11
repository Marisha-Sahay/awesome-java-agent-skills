#!/usr/bin/env python3
"""
Adapter script to convert a SKILL.md into a Cursor .mdc rule file.
Usage:
    python3 adapters/export_to_cursor.py skills/clean-code/java-clean-code/SKILL.md .cursor/rules/
"""

import sys
import os
import re

def convert_skill_to_mdc(skill_path, output_dir):
    if not os.path.exists(skill_path):
        print(f"Error: File {skill_path} not found.")
        sys.exit(1)

    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract name from YAML frontmatter
    match = re.search(r"name:\s*(.+)", content)
    skill_name = match.group(1).strip() if match else "java-rule"
    
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, f"{skill_name}.mdc")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Successfully exported {skill_path} -> {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 export_to_cursor.py <SKILL.md path> <output_dir>")
        sys.exit(1)
    
    convert_skill_to_mdc(sys.argv[1], sys.argv[2])
