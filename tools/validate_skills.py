#!/usr/bin/env python3
"""
Validator for awesome-java-agent-skills SKILL.md files.

Checks each skill's YAML frontmatter against the Agent Skills spec
(https://agentskills.io/specification) plus this repo's conventions:

- `name` and `description` are required.
- `name` is 1-64 lowercase letters, digits and single hyphens, and matches
  the skill's directory name.
- `description` is at most 1024 characters and starts with "Use when", so an
  agent can tell from the description alone when to load the skill.
- An unquoted `description` must not contain ": " or " #", which break YAML.
- Top-level fields outside the spec produce a warning, not an error.

Usage:
    python3 tools/validate_skills.py [skills_dir]
"""

import os
import re
import sys

SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
DESCRIPTION_PREFIX = "Use when"
BLOCK_SCALAR_INDICATORS = {"|", ">", "|-", ">-", "|+", ">+"}


def parse_frontmatter(content):
    """Return {key: (value, style)} for top-level frontmatter keys, or None if absent.

    style is "block" for | or > scalars, "quoted" for quoted values, else "plain".
    """
    match = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", content, re.DOTALL)
    if not match:
        return None

    fields = {}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        key_match = re.match(r"^([A-Za-z0-9_-]+)[ \t]*:(?:[ \t]+(.*))?$", lines[index])
        index += 1
        if not key_match:
            continue
        key = key_match.group(1)
        value = (key_match.group(2) or "").strip()
        if value in BLOCK_SCALAR_INDICATORS:
            parts = []
            while index < len(lines) and (lines[index][:1] in (" ", "\t") or not lines[index].strip()):
                parts.append(lines[index].strip())
                index += 1
            fields[key] = (" ".join(part for part in parts if part), "block")
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            fields[key] = (value[1:-1], "quoted")
        else:
            fields[key] = (value, "plain")
    return fields


def validate_skill_file(path):
    """Return (errors, warnings) for one SKILL.md file."""
    with open(path, "r", encoding="utf-8") as skill_file:
        fields = parse_frontmatter(skill_file.read())
    if fields is None:
        return ["missing or malformed YAML frontmatter (it must open and close with ---)"], []

    errors = []
    warnings = []

    name = fields.get("name", ("", ""))[0]
    description, description_style = fields.get("description", ("", ""))

    if not name:
        errors.append("missing required field 'name'")
    else:
        directory_name = os.path.basename(os.path.dirname(path))
        if len(name) > MAX_NAME_LENGTH or not NAME_PATTERN.match(name):
            errors.append(
                f"name '{name}' must be 1-{MAX_NAME_LENGTH} lowercase letters, digits "
                "and single hyphens"
            )
        if name != directory_name:
            errors.append(f"name '{name}' must match its directory name '{directory_name}'")

    if not description:
        errors.append("missing required field 'description'")
    else:
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(
                f"description is {len(description)} characters; the limit is "
                f"{MAX_DESCRIPTION_LENGTH}"
            )
        if not description.startswith(DESCRIPTION_PREFIX):
            errors.append(
                f"description must start with '{DESCRIPTION_PREFIX}' and say when an agent "
                "should load the skill"
            )
        if description_style == "plain" and (": " in description or " #" in description):
            errors.append(
                "description contains ': ' or ' #', which breaks YAML unless the value is quoted"
            )

    unknown_fields = sorted(set(fields) - SPEC_FIELDS)
    if unknown_fields:
        warnings.append(
            f"top-level fields {unknown_fields} are not in the Agent Skills spec; "
            "put extra data under 'metadata'"
        )

    return errors, warnings


def find_skill_files(skills_dir):
    paths = []
    for root, _, files in os.walk(skills_dir):
        paths.extend(os.path.join(root, name) for name in files if name.lower() == "skill.md")
    return sorted(paths)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo_root, "skills")

    skill_files = find_skill_files(skills_dir)
    if not skill_files:
        print(f"No SKILL.md files found in {skills_dir}")
        sys.exit(1)

    failed = 0
    for path in skill_files:
        errors, warnings = validate_skill_file(path)
        print(f"Checking {os.path.relpath(path, skills_dir)}...")
        for warning in warnings:
            print(f"  ⚠️  Warning: {warning}")
        for error in errors:
            print(f"  ❌ Error: {error}")
        if errors:
            failed += 1
        else:
            print("  ✅ Valid!")

    if failed:
        print(f"\n{failed} of {len(skill_files)} skill files failed validation.")
        sys.exit(1)

    print("\n🎉 All skill files passed validation!")


if __name__ == "__main__":
    main()
