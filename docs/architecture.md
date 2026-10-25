# Architecture

DSH Design Workbench is an installable DSH bundle. `package.json` declares `dsh.bundle.patch`, `cordis.patch.yml` inserts the plugin entrypoint into a profile, and `index.js` registers the Markdown Skills via the host's `ctx.skills` runtime service.

The source instructions live at `.dsh/skills/<name>/SKILL.md`. At plugin activation, the entrypoint reads each file from the installed package, checks its name/description frontmatter, and registers the body in memory. No custom API server, telemetry client, credential store, or third-party runtime dependency is included.

The optional `scripts/install.sh` supports direct copying into `.dsh/skills/` for local authoring or hosts using filesystem discovery directly. That is a secondary path, not the recommended DSH bundle install method.
