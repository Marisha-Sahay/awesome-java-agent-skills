#!/usr/bin/env python3
"""
Validator script for awesome-java-agent-skills repository.
Checks that all SKILL.md files contain required YAML frontmatter fields.
"""

import sys
import os
import re

REQUIRED_FIELDS = ["name", "description", "version", "author", "tags"]

def validate_skill_file(filepath):
    print(f"Checking {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        print(f"  ❌ Error: Missing or malformed YAML frontmatter in {filepath}")
        return False

    frontmatter_text = match.group(1)
    errors = []
    
    for field in REQUIRED_FIELDS:
        if not re.search(fr"^{field}\s*:", frontmatter_text, re.MULTILINE):
            errors.append(field)

    if errors:
        print(f"  ❌ Error: Missing required YAML fields {errors} in {filepath}")
        return False

    print(f"  ✅ Valid!")
    return True

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    skills_dir = os.path.join(repo_root, "skills")

    skill_files = []
    for root, _, files in os.walk(skills_dir):
        for file in files:
            if file.lower() == "skill.md":
                skill_files.append(os.path.join(root, file))

    if not skill_files:
        print(f"No SKILL.md files found in {skills_dir}")
        sys.exit(1)

    all_valid = True
    for sf in skill_files:
        if not validate_skill_file(sf):
            all_valid = False

    if not all_valid:
        sys.exit(1)

    print("\n🎉 All skill files passed validation!")

if __name__ == "__main__":
    main()
