# Contributing

Creator and maintainer: `mulqizamzam`.

## Principles

1. Keep each Skill centered on one repeatable user job.
2. Prefer evidence, explicit assumptions, small changes, and reproducible checks over confident but unverified claims.
3. Do not claim tool use, tests, browser inspection, or file changes unless the host actually performed them.
4. Treat reads/searches as the default discovery phase. Keep edits, writes, shell mutations, dependency changes, and external actions behind an explicit request or authorization.
5. Do not add services, network calls, telemetry, dependencies, credentials, or an MCP server without a concrete requirement and a separate review.
6. Preserve native DSH layout: `.dsh/skills/<kebab-case-name>/SKILL.md`.
7. Keep creator attribution as `mulqizamzam`; do not import other products' branding or documentation.

## Change workflow

1. Read the relevant Skill, compatibility documentation, and tests.
2. Make the smallest change that solves the stated problem.
3. Run `python3 scripts/validate_bundle.py`, `python3 -m unittest discover -s tests -v`, `bash -n scripts/install.sh`, and `bash tests/test_installer.sh`.
4. Build the release package twice and compare SHA-256 hashes when changing packaging or Skill contents.
5. Review diffs for credentials, local absolute paths, private workspace details, stale links, and unsupported runtime claims.
6. Update `CHANGELOG.md` and `VERSION` for a release.

## Skill style

- Keep discovery metadata short and trigger-specific.
- Start instructions with conditions that make the Skill useful.
- Inspect the actual project before prescribing its stack or architecture.
- Make the output shape and completion criteria explicit.
- State what cannot be verified and what evidence would change the conclusion.
