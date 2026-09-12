/*
 * Gradle Quality Gate Template
 * 
 * Instructions:
 * Drop this `build.gradle.kts` content (or the relevant plugin/verification sections) 
 * into your project's `build.gradle.kts` to enforce code quality gates.
 * Make sure you have a `checkstyle.xml` in your repository root or adjust the path accordingly.
 */

plugins {
    java
    checkstyle
    jacoco
}

repositories {
    mavenCentral()
}

dependencies {
    // Add your dependencies here
}

checkstyle {
    toolVersion = "10.12.4"
    configFile = file("${rootDir}/checkstyle.xml")
}

// Bind checkstyle to the standard build lifecycle (usually it's bound automatically to the `check` task)
tasks.withType<Checkstyle> {
    reports {
        xml.required.set(false)
        html.required.set(true)
    }
}

tasks.test {
    useJUnitPlatform()
    finalizedBy(tasks.jacocoTestReport) // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test) // tests are required to run before generating the report
    finalizedBy(tasks.jacocoTestCoverageVerification)
}

tasks.jacocoTestCoverageVerification {
    violationRules {
        rule {
            limit {
                counter = "LINE"
                value = "COVEREDRATIO"
                minimum = "0.80".toBigDecimal()
            }
        }
        rule {
            limit {
                counter = "BRANCH"
                value = "COVEREDRATIO"
                minimum = "0.75".toBigDecimal()
            }
        }
    }
}

// Ensure coverage verification runs during the check phase
tasks.check {
    dependsOn(tasks.jacocoTestCoverageVerification)
}
