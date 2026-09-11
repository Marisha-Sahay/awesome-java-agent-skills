# Awesome Java Agent Skills 🚀

[![Validate Skills](https://github.com/Marisha-Sahay/awesome-java-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/Marisha-Sahay/awesome-java-agent-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated, production-ready collection of **AI Agent Skills**, **Checkstyle rulesets**, and **Maven quality gates** tailored for Java developers. Designed to ground AI agents (Claude, Antigravity, Cursor, Windsurf, Copilot, etc.) in enterprise Java 21 standards, Effective Java practices, and clean code principles.

---

## 📂 Repository Structure

```text
awesome-java-agent-skills/
├── .github/
│   └── workflows/
│       └── validate-skills.yml              # CI workflow verifying SKILL.md format & syntax
├── adapters/
│   └── export_to_cursor.py                  # Helper tool to convert SKILL.md -> Cursor .mdc rules
├── skills/                                  # Core skills categorized by domain
│   ├── clean-code/
│   │   └── java-clean-code/
│   │       └── SKILL.md                     # Java 21 engineering standards & application guidelines
│   ├── framework-spring/                      # Spring Boot 3 & Security (Coming soon)
│   ├── testing-quality/                     # JUnit 5 & ArchUnit (Coming soon)
│   └── jvm-performance/                     # Concurrency & Virtual Threads (Coming soon)
├── templates/
│   └── quality-gates/
│       ├── checkstyle.xml                   # Google Style Checkstyle ruleset
│       └── pom.xml                          # Maven build template (Checkstyle + JaCoCo 80% coverage)
├── tools/
│   └── validate_skills.py                   # Local validation script for SKILL.md schema
├── CONTRIBUTING.md                          # Guide to creating and contributing skills
└── LICENSE                                  # MIT License
```

---

## 🛠️ Usage & Installation

### 1. Claude / Antigravity
Copy the skill folder into your agent skills directory:
```bash
cp -r skills/clean-code/java-clean-code ~/.gemini/antigravity/skills/
```

### 2. Cursor (.mdc Rules)
Use the adapter script to export any skill to your `.cursor/rules/` directory:
```bash
python3 adapters/export_to_cursor.py skills/clean-code/java-clean-code/SKILL.md .cursor/rules/
```

### 3. Windsurf / GitHub Copilot
Append the contents of the target `SKILL.md` to your workspace instruction file (`.windsurfrules` or `.github/copilot-instructions.md`).

---

## 🌟 Available Skills Catalog

| Category | Skill | Target Java | Description |
| :--- | :--- | :--- | :--- |
| **Clean Code** | [`java-clean-code`](skills/clean-code/java-clean-code/SKILL.md) | Java 21 LTS | Java 21 engineering standards, Google/Oracle style, Effective Java, Top 10 Exception rules, Checkstyle & JaCoCo gates. |

---

## ⚙️ Included Quality Gates & Templates

- **[Checkstyle Configuration](templates/quality-gates/checkstyle.xml)**: Enforces 2-space indents, 100-character line limit, explicit import ordering, K&R braces, and naming rules.
- **[Maven Build Template](templates/quality-gates/pom.xml)**: Pre-configured with `maven-checkstyle-plugin` and `jacoco-maven-plugin` with 80% line and 75% branch coverage quality gates.

---

## 🤝 Contributing

Contributions are welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to add new Java skills or refine existing ones.
