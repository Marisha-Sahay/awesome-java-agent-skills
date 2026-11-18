# Contributing to Awesome Java Agent Skills

Thank you for helping build the definitive repository of Java skills for AI agents!

## 🚀 How to Add a New Skill

1. **Choose a Category:** Locate or create an appropriate folder under `skills/` (e.g., `skills/framework-spring/`, `skills/testing-quality/`).
2. **Create a Skill Directory:** Create a subfolder named after the skill (e.g., `skills/framework-spring/spring-boot-3/`).
3. **Add `SKILL.md`:** Write a `SKILL.md` file following the template below.
4. **Run Validation:** Test your skill locally using `python3 tools/validate_skills.py`.
5. **Submit a Pull Request:** Push your branch and open a PR!

---

## 📝 `SKILL.md` Template

```markdown
---
name: your-skill-name
description: Use when [the tasks, files, annotations or error messages that mean an agent should load this skill].
---

# Skill Title

## Overview
Brief introduction to the skill and domain context.

## When to Apply
- Scenario 1
- Scenario 2

## Core Guidelines & Best Practices
- Practice 1
- Practice 2

## Code Examples
...
```

### Frontmatter rules

`tools/validate_skills.py` enforces these, following the [Agent Skills spec](https://agentskills.io/specification):

- **`name`** (required): 1-64 lowercase letters, digits and single hyphens. It must match the skill's folder name.
- **`description`** (required): one line, at most 1024 characters (aim for under 500), starting with `Use when`.
  - Agents read only the description when deciding whether to load a skill, so list the triggers: the kind of task, the files or annotations involved, and the error messages that signal the problem.
  - Don't summarise the skill's rules in the description. An agent that sees a summary tends to follow it and skip the body.
  - Quote the value if it contains `: ` or ` #`, or YAML will fail to parse it.
- **Optional fields** are the spec's `license`, `compatibility` and `metadata`. Put anything else, such as an author or version, under `metadata`.

Good: `description: Use when writing or changing Spring Boot 3 controllers, services or repositories, or when Spring code uses @Autowired field injection.`

Bad: `description: Teaches an agent how to write modern Spring Boot 3 applications.` (says what it is, not when to use it)
