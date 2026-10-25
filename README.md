# DSH ImpeccableMe

**A focused UI design and frontend engineering Skill bundle for DeepSeek Harness (DSH).**

DSH ImpeccableMe provides eight task-specific workflows for planning, reviewing, refining, documenting, and implementing product interfaces. It is distributed as the native DSH plugin bundle **`dsh-impeccableme`**, which registers the included Markdown Skills with the DSH runtime. The bundle adds no third-party runtime dependencies, API credentials, or custom service.

- **Repository:** [mulqizamzam/dsh-impeccableme](https://github.com/mulqizamzam/dsh-impeccableme)
- **Target runtime:** DeepSeek Harness (DSH) `v0.2.1-rc.2`
- **Package / plugin ID:** `dsh-impeccableme`
- **License:** MIT

## Included Skills

| Skill | Purpose | Typical output |
|---|---|---|
| `project-context` | Establish project context and identify undocumented constraints | A grounded project brief and explicit open questions |
| `interface-blueprint` | Plan a screen, page, or user flow before implementation | Information hierarchy, UI states, component map, and acceptance checks |
| `ui-quality-audit` | Evaluate an interface for usability and implementation risks | Prioritized findings with evidence, impact, and verification steps |
| `visual-refinement` | Improve layout, typography, color, density, and interaction feedback | A focused refinement plan or set of targeted edits |
| `system-documentation` | Document the design system found in an existing codebase | `UI_SYSTEM.md` based on existing tokens and components |
| `ux-content` | Improve interface labels, onboarding, empty states, validation, and errors | Consistent, accessible UI copy and state coverage |
| `frontend-engineering` | Implement UI changes, debug defects, test behavior, or automate routine work | Maintainable changes with explicit test evidence |
| `workspace-operator` | Work safely across a repository and its local files | A read-first workflow with clearly defined mutation boundaries |

The Skills are separated by task so an agent can use a focused workflow instead of one long, general-purpose prompt. They rely on the tools provided by the DSH host; they do not grant additional permissions or claim that a test or browser check ran when it did not.

## Installation

### Requirements

- DeepSeek Harness (DSH) `v0.2.1-rc.2` and the `dsh` CLI.
- `pnpm` available to the DSH plugin installer.
- Network access to fetch this GitHub repository.
- Access to the DSH profile where the bundle will be installed.

### Install into a profile

The following example installs the bundle into the `web` profile. Replace `web` with your target profile name when necessary.

```bash
dsh plugin --profile web add "github:mulqizamzam/dsh-impeccableme#main"
```

Confirm that the bundle appears in the profile configuration, then start or restart the profile:

```bash
dsh --profile web --dump-config | grep dsh-impeccableme
dsh web
```

The `package.json` manifest declares the DSH bundle patch. The patch activates `index.js`, which registers all eight Skills with the runtime Skill registry.

To remove the bundle:

```bash
dsh plugin --profile web remove dsh-impeccableme
```

### Install a local checkout for development

From a local clone, use a link dependency to test changes in a profile:

```bash
dsh plugin --profile web add "link:/absolute/path/to/dsh-impeccableme"
```

## Using the Skills

Describe the task to the agent and name the relevant Skill when useful. For example:

```text
Use project-context to inspect this repository and identify undocumented product
constraints. Do not change application code.

Use interface-blueprint to plan a responsive account settings page. Define loading,
empty, validation, save-success, and save-failure states before implementation.

Use ui-quality-audit to review the checkout flow. Cite relevant files and separate
verified behavior from checks that cannot run in this environment.

Use frontend-engineering to fix the form validation defect, add a regression test,
and run the narrowest relevant test command.

Use system-documentation to document the existing design tokens and reusable components
in UI_SYSTEM.md. Do not invent tokens or components.
```

Planning and auditing requests do not imply permission to modify files. During implementation, follow the repository's conventions and available tests. External integrations may only use tools, endpoints, and credentials that are actually available in the host environment.

## Optional: Copy the Skills directly

The direct-copy installer is an alternative to installing the DSH plugin bundle. Use it only when you want the Markdown Skill files in a project's `.dsh/skills/` directory or your host discovers that directory directly.

```bash
./scripts/install.sh --project /absolute/path/to/your-project
./scripts/install.sh --global
```

This method does not install or activate the DSH plugin bundle. Existing Skills are not overwritten unless `--replace` is supplied. `DSH_HOME` is an optional setting for the installer's global destination.

## Validation and packaging

Run the checks from the repository root:

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
node --check index.js
node tests/test_bundle_entrypoint.mjs
bash -n scripts/install.sh
bash tests/test_installer.sh
```

Create a deterministic ZIP archive with:

```bash
python3 scripts/package_release.py --output /tmp/dsh-impeccableme-0.1.0.zip
```

Automated checks cover bundle structure, Skill metadata, registration through a stub DSH context, installer behavior, and reproducible packaging. They do not replace an end-to-end smoke test in the intended live DSH profile. See [the compatibility notes](docs/compatibility.md) and [validation guide](docs/validation.md).

## Project documentation

- [Architecture](docs/architecture.md)
- [Compatibility](docs/compatibility.md)
- [Usage examples](docs/usage-examples.md)
- [Validation guide](docs/validation.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

## License

DSH ImpeccableMe is released under the MIT License. See [LICENSE](LICENSE) for details.