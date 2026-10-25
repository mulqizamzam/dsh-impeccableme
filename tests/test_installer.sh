#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/project" "$tmp/home"
bash "$ROOT/scripts/install.sh" --project "$tmp/project"
test -f "$tmp/project/.dsh/skills/project-context/SKILL.md"
if bash "$ROOT/scripts/install.sh" --project "$tmp/project" >/dev/null 2>&1; then echo 'expected conflict failure' >&2; exit 1; fi
HOME="$tmp/home" DSH_HOME="$tmp/outside" bash "$ROOT/scripts/install.sh" --global >/dev/null 2>&1 && { echo 'expected unsafe DSH_HOME failure' >&2; exit 1; }
echo 'Installer tests: PASS'
