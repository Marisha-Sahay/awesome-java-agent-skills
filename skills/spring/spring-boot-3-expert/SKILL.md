---
name: spring-boot-3-expert
description: Teaches an agent how to write modern Spring Boot 3 applications.
---

# Spring Boot 3 Expert Skill

This skill provides guidelines and best practices for developing modern Spring Boot 3 applications.

## Dependency Injection
Strictly forbid field injection (using `@Autowired` on fields). You must mandate constructor injection. Use `final` fields and Lombok's `@RequiredArgsConstructor` when appropriate to reduce boilerplate code.

## Architecture
Enforce a strict layered architecture:
- **Controller Layer**: Responsible only for HTTP request mapping and delegating to services.
- **Service Layer**: Contains the core business logic.
- **Repository Layer**: Handles data access and interactions with the database.

## Data Modeling
Mandate the use of Java 14+ `record` types for all DTOs (Data Transfer Objects), Requests, and Responses. This ensures immutability and concise class definitions.

## Configuration
Emphasize the use of `@ConfigurationProperties` for managing application configuration over scattered `@Value` annotations to provide strongly-typed configuration.
