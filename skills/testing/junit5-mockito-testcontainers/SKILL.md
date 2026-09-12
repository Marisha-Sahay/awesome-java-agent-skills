---
name: junit5-mockito-testcontainers
description: Guidelines for writing robust, modern Java tests using JUnit 5, Mockito, and Testcontainers.
---

# Testing Mastery Skill

This skill focuses on best practices for writing high-quality tests in modern Java applications.

## Testing Pattern
Enforce the AAA (Arrange, Act, Assert) or BDD (Given, When, Then) pattern in all tests to ensure tests are highly readable and structured consistently.

## Mocking
Instruct the agent to avoid over-mocking. Mock external boundaries and slow dependencies, but use real domain objects. Avoid mocking simple value types or internal application logic when possible. Use Mockito 5+ for all mocking needs.

## Integration Tests
Mandate the use of **Testcontainers** for database integration testing instead of relying on in-memory databases like H2. This ensures environment parity and prevents bugs that only occur in the production database system.

## Frameworks
Specify JUnit 5 (Jupiter) for the testing framework and Mockito 5+ for mocking.
