---
name: ux-content
description: Use when interface text, labels, forms, onboarding, empty states, validation, errors, or confirmation messages are unclear or inconsistent.
---

# UX content

Make interface language clear, actionable, consistent, and appropriate to the user's context.

## Procedure

1. Identify the user's task, knowledge level, risk, and decision at each point in the flow.
2. Inspect existing terminology, voice/tone guidance, product domain, validation rules, and localization constraints.
3. Prefer concrete labels and verbs. Keep button labels distinct enough to predict their outcome; reserve vague labels such as "Submit" for cases where context makes them clear.
4. Write errors that explain what happened, what the user can do next, and whether entered work was preserved. Do not expose internal implementation details.
5. Cover empty, loading, success, disabled, validation, and recovery states where relevant.
6. Keep content inclusive, translatable, and robust to narrow layouts. Avoid relying on color alone to convey meaning.
7. Preserve legal/security accuracy. Do not invent guarantees, privacy claims, or product capability.
8. Present alternatives with rationale; update code or content files only when requested.

## Output

Return a state-aware content table with current text, proposed text, context/rationale, and implementation notes. Highlight terminology inconsistencies and unresolved product decisions.