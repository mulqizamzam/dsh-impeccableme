# DSH Design Workbench

**A focused UI design and frontend engineering skill pack for DeepSeek Harness.**

Creator and maintainer: **`mulqizamzam`**  
Version: **0.1.0**  
Target runtime: **DeepSeek Harness (DSH) v0.2.1-rc.2**

**Repository:** https://github.com/mulqizamzam/dsh-impeccableme

DSH Design Workbench helps an agent plan, build, inspect, and improve product interfaces with evidence-led workflows. It installs as a native DSH bundle and embeds its eight Skills without third-party runtime dependencies, API keys, a custom service, or a build step. DSH’s plugin installer uses pnpm to fetch the GitHub package.

## What it includes

| Skill | Use it for | Expected result |
|---|---|---|
| `project-context` | Start work in an unfamiliar product or record missing constraints | A grounded project brief and explicit open questions |
| `interface-blueprint` | Plan a page, screen, or user flow before coding | Information hierarchy, states, component map, and acceptance checks |
| `ui-quality-audit` | Review an interface for UX and implementation risks | Prioritized findings with evidence, impact, and verification steps |
| `visual-refinement` | Improve layout, typography, color, density, and interaction feedback | A targeted refinement plan or a verified set of edits |
| `system-documentation` | Document the design system already present in a codebase | `UI_SYSTEM.md` grounded in existing tokens and components |
| `ux-content` | Improve labels, onboarding, empty states, validation, and error copy | Consistent, accessible interface content and state coverage |
| `frontend-engineering` | Implement UI changes, debug issues, test behavior, or automate routine work | Small, maintainable changes with explicit test evidence |
| `workspace-operator` | Work safely across a repository and local files | A read-first, least-surprise workflow with a clear mutation boundary |

The pack separates planning, review, design refinement, content, and engineering so a task can load a narrow workflow rather than a long all-purpose prompt. The Skills use tools supplied by the current DSH host; they do not grant tools or pretend that tests or browser checks ran.

## Compatibility

The package uses DSH's local Skill directory format:

```text
.dsh/skills/<skill-name>/SKILL.md
```

Each Skill has kebab-case metadata (`name`, `description`) and task instructions. The layout is designed for **DSH v0.2.1-rc.2** and does not depend on private registry behavior. The validator checks the documented filesystem and frontmatter shape, but it does not replace a smoke test in a live DSH session. See [compatibility and verification](docs/compatibility.md).

## Install with DSH (recommended)

Install the bundle into the `web` profile using DSH's native plugin manager:

```bash
dsh plugin --profile web add "github:mulqizamzam/dsh-impeccableme#main"
```

The package declares `dsh.bundle` in `package.json`; the bundle patch mounts the plugin entrypoint, which registers all eight Skills in DSH's runtime Skill registry. A plain Git dependency without that bundle manifest would install as a dependency without activating a configuration layer.

After installing, restart the Web profile and verify that the bundle layer is present:

```bash
dsh --profile web --dump-config | grep dsh-impeccableme
dsh web
```

Remove it with:

```bash
dsh plugin --profile web remove dsh-impeccableme
```

### Local development install

From a local checkout, the same plugin bundle can be linked into a profile:

```bash
dsh plugin --profile web add "link:/absolute/path/to/dsh-impeccableme"
```

### Optional: copy Skills directly

If you only want the standalone Markdown instructions rather than an installed bundle, you can still copy them into a project's `.dsh/skills/` directory with the helper installer:

```bash
./scripts/install.sh --project /absolute/path/to/your-project
./scripts/install.sh --global
```

The direct-copy method is not the recommended bundle installation. It is useful for local authoring or for hosts that discover `.dsh/skills/` directly without installing bundle plugins. Existing Skills are not overwritten unless `--replace` is supplied.

## Use it

Invoke a Skill by describing the job and, where helpful, naming the Skill. Examples:

```text
Use project-context to inspect this repository and identify product constraints that are
not documented yet. Do not change application code.

Use interface-blueprint to plan a responsive account settings page. Include loading,
empty, validation, save-success, and save-failure states before implementation.

Use ui-quality-audit to review the checkout flow. Cite relevant files and distinguish
verified behavior from checks that cannot run in this environment.

Use frontend-engineering to fix the form validation bug, add a regression test, and run
the narrowest relevant test command.

Use system-documentation to map the existing design tokens and reusable components into
UI_SYSTEM.md. Do not invent tokens or components that are not in the repository.
```

Skills are repeatable workflows, not autonomous permission grants. A request to plan or audit does not imply permission to modify files. For implementation, use the project's conventions and existing tests; for external integrations, only use tools, endpoints, and credentials actually available in the host.

## Prerequisites and configuration

- **Required:** DeepSeek Harness v0.2.1-rc.2, the `dsh` CLI, pnpm available to that CLI, and access to the target profile.
- **For runtime use:** no extra package dependencies, API keys, or environment variables are required by this bundle. DSH profile installation itself uses pnpm.
- **For development:** Node.js is needed to run the bundle-entrypoint test; Python 3 and a POSIX shell are needed for the optional validator, packager, and direct-copy installer.
- **Environment variables:** none required by the plugin. `DSH_HOME` is an optional setting for the separate direct-copy global installer.

The Skill instructions do not make network requests or collect telemetry. Installing the GitHub bundle requires network access to fetch the repository. If your DSH environment exposes only read-only tools, the workflows remain useful for planning and review but cannot apply code changes.

## Verify the package

From the repository root:

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
bash tests/test_installer.sh
```

Create a deterministic ZIP release:

```bash
python3 scripts/package_release.py --output /tmp/dsh-design-workbench-0.1.0.zip
```

Packaging and validation details are in [docs/validation.md](docs/validation.md). These checks validate the bundle structure and safety properties; runtime smoke testing must be performed in the intended DSH installation.

## Bundle layout

```text
package.json                 DSH bundle manifest (`dsh.bundle.patch`)
cordis.patch.yml             Activates the bundle entrypoint in the profile
index.js                     Registers all eight instructions in `ctx.skills`
.dsh/skills/                 Source Markdown for the eight embedded Skills
assets/                      Original light/dark mark and compact icon
scripts/install.sh           Optional direct-copy installer
scripts/validate_bundle.py    Dependency-free structural/safety validator
scripts/package_release.py   Deterministic ZIP packager
tests/                       Structural tests and manual reviewer scenarios
docs/                        Architecture, compatibility, safety, brand, validation
.github/workflows/            Reproducible CI checks
```

## Maintenance

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing the Skill set. See [CHANGELOG.md](CHANGELOG.md) for release history and [SECURITY.md](SECURITY.md) for the reporting and safety boundary.

## License

Released under the MIT License. See [LICENSE](LICENSE).