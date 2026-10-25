---
name: frontend-engineering
description: Use when implementing UI changes, reproducing frontend bugs, adding regression tests, improving interaction resilience, or automating routine repository engineering work.
---

# Frontend engineering

Make maintainable changes backed by evidence.

## Operating sequence

1. Read repository instructions, README, build metadata, implementation, tests, and lockfile before choosing commands or dependencies.
2. For bugs, record observed/expected behavior, reproduction, environment, and logs. If not reproducible, list hypotheses with confidence rather than asserting a cause.
3. Trace the state/data/event path. Prefer a minimal correction that addresses the root cause and preserves unrelated changes.
4. Handle relevant loading, empty, validation, error, disabled, success, and recovery states.
5. Preserve semantics, keyboard behavior, focus, accessible naming, and responsive layouts.
6. Add regression coverage, run the narrowest meaningful test, then broader relevant checks.
7. Inspect unfamiliar scripts before execution. Do not run release, deploy, data deletion, external writes, or credential-sensitive operations without explicit authorization.
8. Use only verified APIs, environment variables, tools, and dependencies. Never fabricate test output.

## Debugging method

Form hypotheses from evidence, choose the least invasive discriminating observation, change one causal surface at a time, add a regression case, and verify adjacent behavior.

## Completion criteria

The requested change is implemented, relevant checks were run, and verification gaps are explicit. If mutation was not authorized or tools are unavailable, provide a concrete patch plan instead.