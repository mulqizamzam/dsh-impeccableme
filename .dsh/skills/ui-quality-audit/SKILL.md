---
name: ui-quality-audit
description: Use when reviewing an existing interface for usability, accessibility, responsive layout, content clarity, performance, or frontend implementation risks.
---

# UI quality audit

Run an evidence-led review of the actual interface and its implementation.

## Procedure

1. Establish scope: named route/screen, device sizes, key journey, and whether the user requests static review or executed checks.
2. Inspect relevant source, existing tests, design tokens, and available screenshots/browser output. Never imply you inspected a screen that was not available.
3. Check hierarchy and scanability, labels and action clarity, empty/loading/error/success states, focus and keyboard use, semantic controls, responsive overflow, contrast and motion, and avoidable rendering/performance risks.
4. Prefer reproducible evidence: file and line references, a minimal reproduction, viewport details, DOM/browser observation, or a test result. Mark checks that require unavailable tools as unverified.
5. Classify each finding by severity and user impact. Distinguish confirmed defects from hypotheses and subjective design opportunities.
6. Recommend a smallest safe correction and a verification method for every actionable finding. Do not edit files unless implementation is authorized.

## Finding format

- **Severity and issue**
- **Evidence**
- **User impact**
- **Recommendation**
- **Verification**
- **Confidence / limitations**

Order findings by impact, not by how easy they are to describe. Avoid filler and generic best-practice lists when there is no project-specific evidence.