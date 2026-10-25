---
name: system-documentation
description: Use when a codebase needs an accurate inventory of existing design tokens, components, patterns, and usage guidance.
---

# System documentation

Document the system that actually exists.

## Procedure

1. Inspect package metadata, CSS variables, theme files, component exports, shared styles, and repeated patterns.
2. Separate verified tokens/components from inferred groupings and future recommendations.
3. Record names, sources, values, usage, variants, responsive behavior, and accessibility requirements when evidence exists.
4. Identify duplication and inconsistency without silently changing implementation.
5. Use an existing docs location/format. Otherwise propose a document such as UI_SYSTEM.md and check for conflicts before writing.
6. Link claims to source files. Label unknown values as unknown rather than estimating.

## Output

Provide a source-grounded inventory of foundations, components, patterns, state conventions, gaps, and maintenance recommendations.

## Completion

A teammate can trace documented facts to code; no invented component or token is presented as established practice.