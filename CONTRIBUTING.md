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
description: A concise 1-2 sentence description of what this skill does.
version: 1.0.0
author: Your Name
tags:
  - java
  - your-tag
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
