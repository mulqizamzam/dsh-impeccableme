# Audit checklist

Use selectively; record evidence and skip irrelevant checks.

## Task and hierarchy
- Is the primary user goal apparent?
- Are labels and primary actions specific and predictable?
- Is important information ordered by decision relevance?
- Are destructive or irreversible actions distinguishable and recoverable?

## States and content
- Are loading, empty, error, validation, success, and disabled states covered where relevant?
- Is error content actionable and associated with the field or operation?
- Are values preserved after failure when appropriate?
- Does text wrap under localization, zoom, and long user-generated content?

## Accessibility
- Are controls named and keyboard-operable?
- Is focus visible and unobscured?
- Are headings and landmarks meaningful?
- Are errors announced and programmatically associated?
- Are contrast and target size adequate?
- Does reduced-motion preference avoid unnecessary movement?

## Responsive behavior
- Does the interface work at narrow and wide widths without unintended horizontal scroll?
- Do tables, dialogs, navigation, and dense controls have a small-screen strategy?
- Do sticky elements avoid covering content or focus?

## Engineering and performance
- Are loading and failure paths bounded and understandable?
- Are expensive renders, assets, requests, or layout shifts justified?
- Are race conditions, repeated submission, stale state, and concurrency addressed?
- Are tests aligned with critical behavior?

## Reporting
Every finding needs evidence, severity, user impact, a focused fix, and a verification plan. State which checks were not possible.