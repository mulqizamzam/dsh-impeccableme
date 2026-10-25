# Security Policy

Maintainer: `mulqizamzam`.

This package contains instruction-only DSH Skills, an installer, and dependency-free validation/packaging utilities. It does not include a service, credential store, telemetry client, or network integration.

Project installation writes to the target project's `.dsh/skills/`; global installation writes beneath the user's DSH home and rejects a destination outside the home directory. Existing Skills are not replaced without `--replace`. Do not expose secrets in logs or execute destructive operations without explicit authorization.

Report suspected vulnerabilities through a private channel controlled by the repository owner when available. Do not publish credentials or sensitive reproduction details in public issues.
