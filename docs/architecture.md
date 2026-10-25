# Architecture

DSH Design Workbench is a skills-only package. DSH discovers each workflow from `.dsh/skills/<skill-name>/SKILL.md`. The repository includes eight focused workflows and no MCP server, network service, or runtime dependency. The installer copies Skills into project or user scopes. Validation and packaging are separate maintenance tools.

## Execution boundaries

The package guides work through host tools available to DSH. It does not confer filesystem, shell, browser, or network permissions. Read-only discovery is the default; editing and external actions require suitable tools and user authorization.
