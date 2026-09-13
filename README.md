# Awesome Java Agent Skills 🚀

[![Validate Skills](https://github.com/Marisha-Sahay/awesome-java-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/Marisha-Sahay/awesome-java-agent-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, production-ready library of **AI Agent Skills**, **Checkstyle rulesets**, and **Maven quality gates** tailored for Java developers. 

Designed to ground AI coding assistants (Claude, Antigravity, Cursor, Windsurf, Copilot) in enterprise Java 21 standards, Effective Java practices, and clean code principles.

## 📖 The "Why"
AI agents write *okay* Java out of the box, but they often hallucinate outdated APIs, ignore enterprise standards, or write code that fails your CI pipeline's Checkstyle or SonarQube gates.

This repository bridges the gap. By injecting these meticulously crafted "skills" into your AI agent's context, you can force it to act like a Principal Java Engineer who actually cares about:
- **Clean Code & Effective Java**
- **Proper Memory Management & Threading**
- **Modern Spring Boot 3 Paradigms**
- **Zero-Tolerance Quality Gates**

---

## 📑 Table of Contents

- [The "Why"](#-the-why)
- [Why Use These Skills?](#-why-use-these-skills)
- [Repository Structure](#-repository-structure)
- [Usage & Installation](#-usage--installation)
- [🌟 The Skill Catalog (Current & Roadmap)](#-the-skill-catalog-current--roadmap)
- [⚙️ Included Quality Gates & Templates](#️-included-quality-gates--templates)
- [🤝 Contributing](#-contributing)

---

## 💡 Why Use These Skills?

- **Eliminate Hallucinations:** Ground the AI in specific Java 21 LTS APIs (e.g., Virtual Threads, Records, Pattern Matching).
- **Pass CI/CD First Time:** AI code is pre-conditioned to respect 100-character line limits, explicit imports, and strict JavaDoc rules.
- **Enterprise Ready:** Stop your AI from returning "hello world" code. Force it to implement proper exception handling, immutable DTOs, and robust tests.
- **Agent Agnostic:** Use the provided adapters to export skills to Cursor, Windsurf, Antigravity, or Copilot.

---

## 📂 Repository Structure

While many "awesome" repos are just flat lists of links, this repository is a **living library** of configurations and rules.

```text
awesome-java-agent-skills/
├── .github/
│   └── workflows/
│       └── validate-skills.yml              # CI workflow verifying SKILL.md format
├── adapters/
│   └── export_to_cursor.py                  # Helper tool to convert SKILL.md -> Cursor .mdc
├── skills/                                  # Core skills categorized by domain
│   ├── clean-code/
│   │   └── java-clean-code/                 # Available NOW!
│   │       └── SKILL.md                     
│   └── ...                                  # (See Roadmap below)
├── templates/
│   └── quality-gates/
│       ├── checkstyle.xml                   # Google Style Checkstyle ruleset
│       └── pom.xml                          # Maven build template (Checkstyle + JaCoCo 80%)
├── tools/
│   └── validate_skills.py                   # Local validation script for SKILL.md
├── CONTRIBUTING.md                          # Guide to creating and contributing skills
└── README.md
```

---

## 🛠️ Usage & Installation

We support exporting these skills to your favorite AI IDEs or Agents.

### 1. Claude / Google Antigravity
Copy the skill folder directly into your agent's skills directory. The agent natively reads `SKILL.md` files.
```bash
# Example: Adding the Clean Code skill
cp -r skills/clean-code/java-clean-code ~/.gemini/antigravity/skills/
```

### 2. Cursor IDE (`.mdc` Rules)
Use the included adapter script to convert any skill into a Cursor-compatible rule file.
```bash
# Example: Exporting the Clean Code skill to Cursor
python3 adapters/export_to_cursor.py skills/clean-code/java-clean-code/SKILL.md .cursor/rules/
```

### 3. Windsurf / GitHub Copilot
Append the raw contents of the target `SKILL.md` directly into your workspace's instruction file (`.windsurfrules` or `.github/copilot-instructions.md`).

---

## 🌟 The Skill Catalog (Current & Roadmap)

We are actively building out the most comprehensive library of Java agent skills. Star the repository ⭐ to track our progress!

### ✅ Currently Available

| Category | Skill | Target Java | Description |
| :--- | :--- | :--- | :--- |
| **Clean Code** | [`java-clean-code`](skills/clean-code/java-clean-code/SKILL.md) | Java 21 LTS | Java 21 engineering standards, Google/Oracle style, Effective Java, Top 10 Exception rules, Checkstyle & JaCoCo gates. |
| **Spring Ecosystem** | [`spring-boot-3-expert`](skills/spring/spring-boot-3-expert/SKILL.md) | Java 17+ | Modern Spring Boot 3 applications, layered architecture, constructor injection, records for DTOs. |
| **Testing & Quality** | [`junit5-mockito-testcontainers`](skills/testing/junit5-mockito-testcontainers/SKILL.md) | Java 17+ | Testing mastery with JUnit 5, Mockito 5+, and Testcontainers for robust AAA/BDD testing. |
| **Build Tools** | [`maven-dependency-management`](skills/build-tools/maven-dependency-management/SKILL.md) | Java 17+ | Enterprise-grade Maven management: BOMs, transitive exclusions, and dependency convergence. |

### 🚀 Roadmap (Coming Soon)

We will be continually adding new skills. Want to help? See our [Contributing Guide](CONTRIBUTING.md).

- [ ] **Core Java**
  - [ ] `java-concurrency`: Virtual Threads, structured concurrency, CompletableFuture best practices.
  - [ ] `java-collections`: When to use which map/set/list, avoiding memory leaks, stream API mastery.
- [ ] **Spring Ecosystem**
  - [ ] `spring-boot-core`: Constructor injection, avoiding `@Autowired`, proper configuration properties.
  - [ ] `spring-security`: OAuth2, JWT implementation standards, stateless architecture.
  - [ ] `spring-data-jpa`: N+1 problem prevention, proper entity modeling, auditing.
- [ ] **Testing & Quality**
  - [ ] `junit5-mockito`: AAA pattern (Arrange, Act, Assert), parameterized tests, BDD Mockito.
  - [ ] `testcontainers`: Database integration testing without mocks.
  - [ ] `archunit`: Enforcing architectural boundaries via tests.
- [ ] **Cloud Native & Data**
  - [ ] `quarkus-micronaut`: AOT compilation, native image constraints.
  - [ ] `flyway-liquibase`: Database migration best practices, idempotency.

---

## ⚙️ Included Quality Gates & Templates

Alongside the AI skills, we provide drop-in templates to enforce these standards in your build pipeline:

- **[Checkstyle Configuration](templates/quality-gates/checkstyle.xml)**: Enforces 2-space indents, 100-character line limit, explicit import ordering, K&R braces, and strict naming conventions.
- **[Maven Build Template](templates/quality-gates/pom.xml)**: A pre-configured `pom.xml` featuring:
  - `maven-checkstyle-plugin` bound to the `validate` phase.
  - `jacoco-maven-plugin` enforcing an 80% line and 75% branch coverage quality gate.
- **[Gradle Build Template](templates/quality-gates/build.gradle.kts)**: A pre-configured `build.gradle.kts` featuring:
  - `checkstyle` plugin bound to the standard build lifecycle.
  - `jacoco` plugin enforcing an 80% line and 75% branch coverage quality gate.

---

## 🤝 Contributing

We want to make this the ultimate resource for Java developers in the AI era. Contributions are highly welcome! 

Whether you want to write a new skill, fix a typo, or add support for a new AI agent, please read our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

<p align="center">
  <i>Built with ❤️ for the Java and AI engineering community.</i>
</p>
