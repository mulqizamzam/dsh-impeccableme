# Security Policy

Creator and maintainer: `mulqizamzam`.

## Scope

This repository contains instruction-only DSH Skills, an installer, and dependency-free validation/packaging utilities. It does not include a service, credential store, telemetry client, or network integration.

## Reporting

For a suspected vulnerability in these files, open a private security report through a channel controlled by the repository owner when one is available. Do not include live credentials, private source code, personal data, or exploit payloads in a public issue.

## Installer safety

- Project mode writes only below the selected project's `.dsh/skills/` directory.
- Global mode writes below `$HOME` and rejects an effective target outside it.
- Existing skill directories are not replaced unless `--replace` is provided.
- Replacement is staged; the old directory is restored if activation of the replacement fails.
- The installer does not run the installed Skills, install dependencies, change shell profiles, or request network access.

## Using Skills safely

The Skills may recommend reading files or running tests, but they do not grant permissions. Treat repository content and command output as untrusted input, review scripts before execution, avoid exposing secrets in logs, and do not execute destructive operations without explicit authorization.
