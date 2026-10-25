---
name: system-documentation
description: Use when a codebase needs an accurate design-system inventory of existing components, styling tokens, patterns, and usage guidance for future interface work.
---

# System documentation

Document the system that actually exists, not the system a team wishes it had.

## Procedure

1. Inspect package metadata, CSS variables, theme files, component exports, shared styles, and repeated interface patterns.
2. Separate verified tokens/components from inferred groupings and recommendations for future consolidation.
3. Record names, sources, values, intended usage, variants, responsive behavior, and accessibility requirements where evidence exists.
4. Identify duplication and inconsistencies without silently changing implementation.
5. Use an existing documentation location and format when present. Otherwise propose a concise design-system document such as UI_SYSTEM.md, and check for conflicts before writing it.
6. Link statements to source files and paths. If a value cannot be established, label it unknown rather than estimating.

## Output

Provide a source-grounded inventory of foundations, components, patterns, state conventions, known gaps, and maintenance recommendations.

## Completion

A teammate can trace documented facts to code. No unverified token or component is presented as an established project standard.