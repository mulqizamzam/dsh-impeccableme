# Validation

Run from the repository root:

```bash
python3 scripts/validate_bundle.py
node --check index.js
node tests/test_bundle_entrypoint.mjs
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
bash tests/test_installer.sh
npm pack --dry-run --json
```

The checks cover DSH bundle metadata and patch, the eight source Skills, runtime registration through a stub Cordis context, installer safety, public file scanning, and packaging.

Build two release ZIPs and compare checksums when validating the archive packager:

```bash
python3 scripts/package_release.py --output /tmp/dsh-a.zip
python3 scripts/package_release.py --output /tmp/dsh-b.zip
sha256sum /tmp/dsh-a.zip /tmp/dsh-b.zip
cmp /tmp/dsh-a.zip /tmp/dsh-b.zip
```

The npm pack dry-run confirms the Git-install package includes `package.json`, `index.js`, `cordis.patch.yml`, and each Skill's `SKILL.md`.

Local tests and CI do not replace a live DSH v0.2.1-rc.2 profile smoke test. Verify installation with `dsh plugin --profile web add "github:mulqizamzam/dsh-impeccableme#main"`, inspect the profile dump for the bundle row, then restart `dsh web`.
