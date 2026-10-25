# Validation

Run the package checks from the repository root:

```bash
python3 scripts/validate_bundle.py
node --check index.js
node tests/test_bundle_entrypoint.mjs
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
bash tests/test_installer.sh
```

For a deterministic release ZIP, build it twice and compare the output checksums:

```bash
python3 scripts/package_release.py --output /tmp/dsh-a.zip
python3 scripts/package_release.py --output /tmp/dsh-b.zip
sha256sum /tmp/dsh-a.zip /tmp/dsh-b.zip
cmp /tmp/dsh-a.zip /tmp/dsh-b.zip
```

The npm packaging file set can be inspected without publishing using `npm pack --dry-run --json`; confirm `package.json`, `index.js`, `cordis.patch.yml`, and all eight Skill files are included.

These checks do not replace a full live DSH v0.2.1-rc.2 runtime smoke test or prove that remote CI executed.
