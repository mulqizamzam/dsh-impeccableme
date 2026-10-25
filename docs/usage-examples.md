# Usage examples

Install the bundle into the Web profile:

```bash
dsh plugin --profile web add "github:mulqizamzam/dsh-impeccableme#main"
```

Then invoke the Skill relevant to the task:

- Use `project-context` to identify undocumented constraints before changing code.
- Use `interface-blueprint` to specify responsive layouts and meaningful loading, empty, error, and success states.
- Use `ui-quality-audit` to produce evidence-backed findings with severity and verification steps.
- Use `frontend-engineering` to reproduce a bug, make a minimal patch, add a regression test, and run the narrowest useful checks.
- Use `system-documentation` to map real tokens and components without inventing a design system.

Verify the bundle layer with `dsh --profile web --dump-config | grep dsh-impeccableme`, then restart `dsh web` after installation.
