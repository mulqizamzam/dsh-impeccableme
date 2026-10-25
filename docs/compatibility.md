# Compatibility contract

## Target

- Target runtime: DeepSeek Harness v0.2.1-rc.2.
- Install form: native DSH plugin bundle, managed with `dsh plugin --profile <profile> add <package>`.
- Bundle manifest: `package.json` declares `dsh.bundle.patch` as `./cordis.patch.yml`.
- Bundle patch: adds `dsh-impeccableme` to the selected profile.
- Embedded Skill sources: `.dsh/skills/<kebab-case-name>/SKILL.md`.

The runtime entrypoint loads the Markdown source files from the installed package and registers each using the DSH `ctx.skills` service. This avoids requiring the project filesystem scanner to discover files inside the installed plugin package. The bundle relies on the `skills` service from a standard base-backed DSH composition.

## Install and verify

```bash
dsh plugin --profile web add "github:mulqizamzam/dsh-impeccableme#main"
dsh --profile web --dump-config | grep dsh-impeccableme
dsh web
```

A Git dependency without a `dsh.bundle` manifest can install as an ordinary dependency but will not contribute a profile patch layer.

## Package-level checks

The validator and tests check Skill metadata and directories, package manifest fields, the profile patch, registration of all eight Skills through a stub DSH context, local references, SVG shape/security, common upstream identity markers, secret-shaped values, installer safety, and deterministic packaging.

These checks do not prove that the user's DSH installation can reach GitHub or resolve the bundle successfully in a live profile.

## Live runtime smoke test

After install, inspect the profile dump for the bundle row, restart the Web profile, and ask the agent to invoke `project-context`. The repository tests validate the entrypoint with a stub context; a full session-level smoke test still needs the intended DSH installation.
