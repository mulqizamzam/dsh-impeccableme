---
name: frontend-engineering
description: Use when implementing UI changes, reproducing frontend bugs, adding regression tests, improving interaction resilience, or automating routine repository engineering tasks.
---

# Frontend engineering

Make small, maintainable changes backed by evidence.

## Operating sequence

1. Read repository instructions, README, package/build metadata, relevant implementation, tests, and lockfile before choosing commands or dependencies.
2. For a bug, record observed behavior, expected behavior, reproduction, environment, and logs. If it cannot be reproduced, list hypotheses with confidence rather than naming a cause.
3. Trace the responsible state/data/event path. Prefer the smallest correction that addresses the root cause and preserves unrelated user changes.
4. Handle loading, empty, validation, error, disabled, success, and recovery states relevant to the feature.
5. Preserve semantics, keyboard behavior, focus, accessible naming, and responsive layouts.
6. Add or adjust regression coverage for the defect or requirement. Run the narrowest meaningful test first, then broader relevant checks.
7. Inspect command scripts before executing unfamiliar actions. Do not run release, deploy, data deletion, external writes, or credential-sensitive operations without explicit authorization.
8. Use only verified APIs, environment variables, tool availability, and dependencies. Never fabricate test output.

## Debugging method

Form hypotheses from evidence, choose the least invasive observation that distinguishes them, change one causal surface at a time, add a regression case, and verify adjacent behavior.

## Completion criteria

The requested change is implemented, relevant tests or checks were actually run, and remaining verification gaps are explicitly reported. If code changes were not authorized or tools are unavailable, provide a concrete patch plan instead.