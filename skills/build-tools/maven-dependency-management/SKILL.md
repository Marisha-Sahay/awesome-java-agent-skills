---
name: maven-dependency-management
description: Guidelines for enterprise-grade Maven dependency management.
---

# Maven Dependency Management Skill

This skill focuses on best practices for managing dependencies in enterprise Maven projects. As a strict build engineer, you must enforce the following rules:

## Bill of Materials (BOM) & DependencyManagement
NEVER hardcode versions in the `<dependencies>` block if a BOM (such as `spring-boot-dependencies`) or a `<dependencyManagement>` section can be used. This ensures version consistency across all modules in an enterprise Java project and simplifies upgrades.

## Transitive Dependency Exclusions
Actively identify and exclude conflicting transitive dependencies using the `<exclusions>` tag. 
- Explicitly exclude legacy logging frameworks (e.g., `commons-logging` or `log4j`) in favor of modern facades like `slf4j` and implementations like `logback`.
- Resolve any build failures caused by classpath clashes by excluding the offending transitive dependencies from their root source.

## Dependency Convergence
Require the use of the `maven-enforcer-plugin` configured with the `dependencyConvergence` rule. This will fail the build if there are version conflicts across transitive dependencies, ensuring a stable and predictable classpath—a hallmark of senior Java engineering.
