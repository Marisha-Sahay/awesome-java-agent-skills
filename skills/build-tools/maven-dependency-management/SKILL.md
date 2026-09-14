---
name: maven-dependency-management
description: Guidelines for enterprise-grade Maven dependency management.
---

# Maven Dependency Management Skill

This skill focuses on best practices for managing dependencies in enterprise Maven projects. As a strict build engineer, you must enforce the following rules:

## Bill of Materials (BOM) & DependencyManagement
NEVER hardcode versions in the `<dependencies>` block if a BOM (such as `spring-boot-dependencies`) or a `<dependencyManagement>` section can be used. This ensures version consistency across all modules in an enterprise Java project and simplifies upgrades.

**Example Context:**
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>3.1.5</version> <!-- Use appropriate version -->
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## Transitive Dependency Exclusions
Actively identify and exclude conflicting transitive dependencies using the `<exclusions>` tag. 
- Explicitly exclude legacy logging frameworks (e.g., `commons-logging` or `log4j`) in favor of modern facades like `slf4j` and implementations like `logback`.
- Resolve any build failures caused by classpath clashes by excluding the offending transitive dependencies from their root source.

**Example Context:**
```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-core</artifactId>
    <exclusions>
        <exclusion>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## Dependency Convergence
Require the use of the `maven-enforcer-plugin` configured with the `dependencyConvergence` rule. This will fail the build if there are version conflicts across transitive dependencies, ensuring a stable and predictable classpath—a hallmark of senior Java engineering.

**Example Context:**
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-enforcer-plugin</artifactId>
    <version>3.4.1</version>
    <executions>
        <execution>
            <id>enforce</id>
            <goals>
                <goal>enforce</goal>
            </goals>
            <configuration>
                <rules>
                    <dependencyConvergence/>
                </rules>
            </configuration>
        </execution>
    </executions>
</plugin>
```
