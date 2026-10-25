---
name: interface-blueprint
description: Use when planning a new screen, page, or user flow before implementation, especially when information hierarchy, responsive behavior, or interface states need explicit design.
---

# Interface blueprint

Translate the user goal into an implementable UI plan before changing code.

## Procedure

1. Identify the user task, entry point, primary action, supporting actions, and successful outcome.
2. Inspect existing routes, components, design tokens, content conventions, and responsive patterns. Prefer the current system unless evidence supports a change.
3. Define the information hierarchy and content structure before choosing decoration.
4. Specify layout behavior at narrow, medium, and wide viewports. Include overflow and long-content behavior.
5. Enumerate relevant states: initial/loading, populated, empty, validation, disabled, error, success, and recovery. Include only states meaningful to the feature, and explain omissions.
6. Cover keyboard navigation, semantic structure, visible focus, labels, contrast, motion preferences, and touch targets.
7. Map proposed components to existing reusable components; mark genuinely new components as proposed.
8. Write acceptance checks that can be verified through tests or direct observation.

## Output

Produce the user goal, hierarchy, layout behavior, state matrix, accessibility notes, component map, open decisions, and acceptance criteria.

## Guardrails

Do not implement during the planning phase unless requested. Do not invent design tokens or claim a mockup was tested when it was not.