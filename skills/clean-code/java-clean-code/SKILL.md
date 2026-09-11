---
name: java-clean-code
description: Modern Java 21 LTS engineering standards, Effective Java design patterns, clean code conventions, and build quality gates.
version: 1.0.0
author: Marisha Sahay
tags:
  - java
  - java21
  - clean-code
  - solid
  - effective-java
  - checkstyle
  - jacoco
---

# Java 21 Clean Code & Engineering Standards

## Overview
This skill instructs AI agents to author, refactor, and review enterprise Java code targeting **Java 21 LTS**. It enforces clean code, Effective Java principles, modern language capabilities (Virtual Threads, Records, Pattern Matching), and automated quality gates (Checkstyle & JaCoCo).

## When to Apply
- Writing new Java classes, records, interfaces, or unit tests.
- Refactoring legacy Java codebases.
- Conducting code reviews or static analysis remediation.

---

## 1. Core Architectural & Naming Standards

### Naming Conventions & Anti-Patterns
| Identifier | Style | Format / Rule | Good Example | Bad Anti-Pattern |
| :--- | :--- | :--- | :--- | :--- |
| **Class / Interface / Record / Enum** | PascalCase | Specific, intention-revealing nouns. | `OrderProcessingService` | ❌ `Manager`, `Data`, `IOrderService` |
| **Method** | lowerCamelCase | Verb or verb phrase describing the action. | `calculateTotal()` | ❌ `process()`, `doSave()` |
| **Variable / Field / Parameter** | lowerCamelCase | Concise, mnemonic nouns. Avoid custom abbreviations. | `customerName` | ❌ `mName`, `custMngSys` |
| **Constant** | UPPER_SNAKE_CASE | `static final` deeply immutable values. | `MAX_RETRY_ATTEMPTS` | ❌ `maxRetry` |
| **Package** | Lowercase | Hierarchical, concise, no underscores. | `com.example.order` | ❌ `com.example.order_service` |

### Source File Layout & Ordering
Every `.java` file must follow this exact section sequence (100-character line limit, 2-space indentation, no tabs):
1. **Package Declaration**: Single line, never line-wrapped.
2. **Import Statements**: Alphabetical. Group static imports first, followed by standard imports. **Wildcard imports (`import java.util.*`) are strictly prohibited.**
3. **Class Body Member Order**:
   - `static final` constants -> Static fields -> Instance fields (`private final` prioritized) -> Constructors -> Static factory methods -> Public methods -> Overloaded methods (must be contiguous) -> Private helper methods.

---

## 2. Modern Java 21 LTS Features

- **Virtual Threads (JEP 444)**: Use `Executors.newVirtualThreadPerTaskExecutor()` for high-concurrency I/O-bound tasks. **Never pool virtual threads.** Prefer `ReentrantLock` over `synchronized` to avoid thread pinning during blocking I/O.
- **Records (JEP 395/440)**: Use `record` for immutable data carriers and DTOs.
- **Sealed Classes (JEP 409)**: Use `sealed interface` / `sealed class` to define closed type hierarchies and enable compiler-enforced exhaustive pattern matching.
- **Pattern Matching for Switch (JEP 441)**:
  ```java
  public double calculateArea(Shape shape) {
    return switch (shape) {
      case Circle(double radius) -> Math.PI * radius * radius;
      case Rectangle(double w, double h) when w > 0 && h > 0 -> w * h;
      case Square(double side) when side > 0 -> side * side;
    };
  }
  ```
- **Sequenced Collections (JEP 431)**: Use `getFirst()`, `getLast()`, and `reversed()` on ordered collections instead of manual index calculations.

---

## 3. Object Design & Clean Code Practices

- **Immutability by Default**: Declare fields `private final`. Minimize mutable state. Return unmodifiable collections (`List.of()`, `Set.of()`) and defensive copies.
- **Creation Patterns**: Favor static factory methods (`of()`, `from()`) or Builders for objects with >3 optional parameters. Implement Singletons using single-element `enum`.
- **Composition over Inheritance**: Use delegation and Decorator wrappers rather than extending concrete classes.
- **Generics (PECS)**: Use `Producer-Extends, Consumer-Super` (`Collection<? extends T>` for reading, `Collection<? super T>` for writing).
- **Null Safety**: Never pass or return `null` for collections/arrays (return `List.of()` or empty arrays). Use `Optional<T>` strictly for method return values (never as fields or parameters).

---

## 4. Exception Handling Best Practices

1. **Throw Early, Handle Late**: Validate arguments at boundaries (`Objects.requireNonNull()`, `IllegalArgumentException`). Handle exceptions at boundary layers.
2. **Resource Management**: Always use `try-with-resources` for `AutoCloseable` types.
3. **No Empty Catches or Log & Rethrow**: Never leave catch blocks empty. Choose to either log and resolve **OR** wrap and rethrow—never both (prevents log duplication).
4. **Preserve Root Causes**: Always pass the original exception as the cause when throwing custom domain exceptions (`throw new OrderException("Failed", cause)`).
5. **Protect PII**: Never log passwords, API keys, or personally identifiable information (PII) in error logs.

---

## 5. Documentation & Quality Gates

- **Javadoc**: Required for all `public` and `protected` APIs. First sentence must be a concise summary ending in a period. Tag order: `@param`, `@return`, `@throws`, `@deprecated`. Always use `@Override`.
- **Checkstyle Enforcement**: Code must compile with zero style violations (Google Style Guide, 2-space indent, K&R braces).
- **JaCoCo Quality Gates**: Unit tests (JUnit 5 + AssertJ/Mockito) must maintain minimum **80% Line Coverage** and **75% Branch Coverage** on business logic.
