---
name: ui-quality-audit
description: Use when reviewing an existing interface for usability, accessibility, responsive layout, content clarity, performance, or frontend implementation risks.
---

# UI quality audit

Run an evidence-led review of the actual interface and its implementation.

## Procedure

1. Establish scope: route/screen, device sizes, key journey, and whether static review or executed checks are requested.
2. Inspect relevant source, tests, design tokens, and available screenshots/browser output. Never imply you inspected a screen that was unavailable.
3. Check hierarchy, action clarity, empty/loading/error/success states, keyboard/focus use, semantic controls, responsive overflow, contrast/motion, and avoidable performance risks.
4. Prefer reproducible evidence: file/line references, a minimal reproduction, viewport details, browser observation, or test result. Mark checks requiring unavailable tools as unverified.
5. Classify findings by severity and user impact. Distinguish confirmed defects from hypotheses and subjective design opportunities.
6. Recommend a smallest safe correction and verification method. Do not edit unless implementation is authorized.

## Finding format

- **Severity and issue**
- **Evidence**
- **User impact**
- **Recommendation**
- **Verification**
- **Confidence / limitations**

Order findings by impact. Avoid generic best-practice lists unsupported by project evidence.