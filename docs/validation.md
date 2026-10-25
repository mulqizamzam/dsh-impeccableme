# Validation

Run `python3 scripts/validate_bundle.py`, `python3 -m unittest discover -s tests -v`, `bash -n scripts/install.sh`, and `bash tests/test_installer.sh`. For reproducibility, build two ZIPs with `scripts/package_release.py` and compare their SHA-256 checksums. These checks do not replace a live DSH smoke test or CI execution.
