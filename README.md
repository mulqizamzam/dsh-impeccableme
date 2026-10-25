# DSH Design Workbench

**A focused UI design and frontend engineering Skill pack for DeepSeek Harness.**

Creator and maintainer: **`mulqizamzam`**  
Version: **0.1.0**  
Target runtime: **DeepSeek Harness (DSH) v0.2.1-rc.2**

DSH Design Workbench helps an agent plan, build, inspect, and improve product interfaces with evidence-led workflows. It installs as native DSH Skills: no service, API key, build step, package manager, or third-party runtime dependency is required.

## Included Skills

- `project-context` — discover product goals, user needs, constraints, and open questions.
- `interface-blueprint` — plan screens, flows, layout, states, and acceptance criteria.
- `ui-quality-audit` — review usability, accessibility, responsiveness, and implementation risks.
- `visual-refinement` — improve visual hierarchy, spacing, typography, and interaction feedback.
- `system-documentation` — document existing design tokens and reusable components.
- `ux-content` — improve labels, onboarding, validation, empty states, and errors.
- `frontend-engineering` — implement, debug, test, and automate frontend work.
- `workspace-operator` — inspect and modify repository files with a read-first safety boundary.

## Install

Install into a project:

```bash
./scripts/install.sh --project /absolute/path/to/your-project
```

Install for the current user:

```bash
./scripts/install.sh --global
```

Install a single Skill:

```bash
./scripts/install.sh --project /absolute/path/to/your-project --skill ui-quality-audit
```

The installer refuses to overwrite existing Skills by default. Use `--replace` only after reviewing the existing Skill and intending to replace it. Global installation uses `${DSH_HOME:-$HOME/.dsh}/skills/`; `DSH_HOME` is optional and the installer rejects global destinations outside the user's home directory.

## Verify

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
bash tests/test_installer.sh
```

Create a deterministic ZIP:

```bash
python3 scripts/package_release.py --output /tmp/dsh-design-workbench-0.1.0.zip
```

## Compatibility and limitations

The package layout follows DSH local Skill discovery: `.dsh/skills/<skill-name>/SKILL.md`. It targets DSH v0.2.1-rc.2. Validation checks metadata, directory structure, local references, branding files, and common secret patterns, but a live DSH session smoke test remains a separate step. Skills use only host capabilities available to the current runtime; they do not grant tools or permissions.

No services, telemetry, or outbound network calls are included in the Skills. No external runtime dependencies are required for installation; included validator and packager scripts use Python's standard library and the installer uses POSIX shell utilities.

## Repository contents

- `.dsh/skills/` — eight DSH-native Skills.
- `scripts/install.sh` — guarded project/global installer.
- `scripts/validate_bundle.py` — dependency-free structural and safety validator.
- `scripts/package_release.py` — deterministic ZIP packaging.
- `tests/` — automated checks and reviewer scenarios.
- `docs/` — architecture, compatibility, brand, usage, and validation.
- `.github/workflows/validate.yml` — CI checks for validator, tests, installer, and reproducible packaging.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), and [SECURITY.md](SECURITY.md) for maintenance and security details. Released under MIT; see [LICENSE](LICENSE).
