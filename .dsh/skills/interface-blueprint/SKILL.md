---
name: interface-blueprint
description: Use when planning a new screen, page, or user flow before implementation, especially when hierarchy, responsive behavior, or interface states need explicit design.
---

# Interface blueprint

Translate the user goal into an implementable UI plan before changing code.

## Procedure

1. Identify the user task, entry point, primary action, supporting actions, and successful outcome.
2. Inspect existing routes, components, design tokens, content conventions, and responsive patterns. Prefer the current system unless evidence supports a change.
3. Define information hierarchy and content structure before decoration.
4. Specify behavior at narrow, medium, and wide viewports, including overflow and long content.
5. Enumerate relevant loading, populated, empty, validation, disabled, error, success, and recovery states. Explain meaningful omissions.
6. Cover keyboard navigation, semantic structure, visible focus, labels, contrast, motion preferences, and touch targets.
7. Map proposed components to existing reusable components; mark genuinely new components as proposals.
8. Write acceptance checks that can be verified through tests or direct observation.

## Output

Produce the user goal, hierarchy, layout behavior, state matrix, accessibility notes, component map, open decisions, and acceptance criteria.

## Guardrails

Do not implement during planning unless requested. Do not invent design tokens or claim a mockup was tested when it was not.