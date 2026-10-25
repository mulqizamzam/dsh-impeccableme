---
name: ux-content
description: Use when interface text, labels, forms, onboarding, empty states, validation, errors, or confirmation messages are unclear or inconsistent.
---

# UX content

Make interface language clear, actionable, consistent, and context-appropriate.

## Procedure

1. Identify the user's task, knowledge level, risk, and decision at each flow step.
2. Inspect terminology, voice/tone guidance, product domain, validation rules, and localization constraints.
3. Prefer concrete labels and verbs. Button labels should predict their outcomes.
4. Write errors that explain what happened, what users can do next, and whether entered work was preserved. Avoid exposing internal implementation details.
5. Cover empty, loading, success, disabled, validation, and recovery states where relevant.
6. Keep content inclusive, translatable, and robust to narrow layouts. Do not rely on color alone.
7. Preserve legal/security accuracy; do not invent guarantees or product capabilities.
8. Present alternatives with rationale. Update code/content only when requested.

## Output

Return a state-aware table with current and proposed text, context/rationale, implementation notes, terminology inconsistencies, and unresolved decisions.