---
name: java-build-verification
description: Use when about to tell the user that Java code works, tests pass, a Maven or Gradle build is green, a flaky test is fixed, or a change is ready to merge or commit.
---

# Java Build Verification

## Overview

A claim about a Java build is worth exactly the build output behind it. Before saying tests pass, a
flaky test is fixed or a change is ready to merge, run the command that proves it and quote its
summary lines in your reply.

## The Verification Block

Every message that reports a build, test or fix outcome ends with this block. Fill each line with
text copied from tool output you received in this session:

```markdown
**Verification**
- Command: `./mvnw verify` (exit 0)
- Unit tests (Surefire): Tests run: 10, Failures: 0, Errors: 0, Skipped: 0
- Integration tests (Failsafe): Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
- Quality gates: All coverage checks have been met.
- Result: BUILD SUCCESS
```

- A line you have no output for reads `not run`, and the message makes no claim that depends on it.
- Test counts come from Maven's `Tests run:` summary lines, never from counting `@Test` methods.
- The exit code is the build command's own, not that of a `tail` or `grep` it was piped into.
- A flaky-test fix adds a `Repeat runs` line with the before and after numbers (see below).

## Getting the Evidence

Run the build into a fresh log file and read the summary lines from it, in one shell command:

```bash
log=$(mktemp); ./mvnw verify > "$log" 2>&1; echo "exit=$? log=$log"
grep -E '^\[(INFO|WARNING|ERROR)\] (Tests run: [0-9]+, Failures: [0-9]+, Errors: [0-9]+, Skipped: [0-9]+$|BUILD |Rule violated|All coverage)|^\[ERROR\]   ' "$log"
```

A passing build prints one `Tests run:` line per plugin, the coverage line and `BUILD SUCCESS`. A
failing build also prints one `[ERROR]   Class.method:line` entry per failing test. For follow-up
greps, use the path printed after `log=`. Each build gets its own file because a fixed path such as
`/tmp/verify.log` is shared by every build on the machine: with parallel agents or worktrees you end
up quoting another build's numbers.

### Which command proves what

| Claim | Command | What it runs |
|---|---|---|
| Unit tests pass | `./mvnw test` | Compile, Surefire (`*Test`) |
| Ready to merge / CI will pass | `./mvnw verify`, or whatever the CI workflow runs | Surefire, Failsafe (`*IT`), and gates bound to `verify` such as the JaCoCo check |
| One unit test | `./mvnw test -Dtest='RefundServiceTest#rejectsAnUnknownOrder'` | That test only |
| One integration test | `./mvnw -q test-compile` then `./mvnw failsafe:integration-test failsafe:verify -Dit.test=RefundEventsIT` | That IT only (`-Dtest` does not select Failsafe tests) |
| Gradle | `./gradlew check`; one test: `./gradlew test --tests 'RefundServiceTest'` | Evidence is `BUILD SUCCESSFUL` plus the exit code; counts are in `build/test-results/` |

## Flaky Test Fixes

One green run of a test that failed one time in five proves nothing: the unfixed test passes most
runs too. Measure, fix, measure again:

```bash
./mvnw -q test-compile
fails=0; for i in $(seq 1 20); do
  ./mvnw -q failsafe:integration-test failsafe:verify -Dit.test=RefundEventsIT > /dev/null 2>&1 || fails=$((fails+1))
done; echo "failures: $fails/20"
```

(For a unit test, loop `./mvnw -q surefire:test -Dtest=OrderServiceTest` instead.)

1. Run the loop on the unfixed code. If it never fails, you have not reproduced the flake: say so,
   and treat any fix as unconfirmed.
2. Apply the fix, run `./mvnw -q test-compile` again, then the same loop.
3. Report both: `Repeat runs: 5/20 failed before the fix, 0/20 after`.

Run enough repetitions that the old failure rate would almost surely show up:

| Observed failure rate | Runs |
|---|---|
| 1 in 3 | 12 |
| 1 in 5 | 20 |
| 1 in 10 | 45 |

## Common Mistakes

These come from baseline runs of agents working without this skill:

| What the agent did | What the Verification block shows instead |
|---|---|
| Wrote "the test ran once with no failures" without running Maven | `Command: not run` and no pass claim |
| Ran `./mvnw -q verify \| tail -30` and read "no errors visible" as a pass | The `Tests run:` and `BUILD SUCCESS` lines from the log |
| Reported "13 tests pass" by counting test methods | The two `Tests run:` lines Maven printed |
| Said "I fixed the flaky test" after one green run | `Repeat runs: 5/20 failed before the fix, 0/20 after` |
| Grepped a shared `/tmp/verify.log` that a parallel build had overwritten, and reported its counts | Counts from this build's own `mktemp` log |
