#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/project" "$tmp/home"
bash "$ROOT/scripts/install.sh" --project "$tmp/project"
test -f "$tmp/project/.dsh/skills/project-context/SKILL.md"
test -f "$tmp/project/.dsh/skills/workspace-operator/SKILL.md"
if bash "$ROOT/scripts/install.sh" --project "$tmp/project" >/dev/null 2>&1; then
  echo "expected conflict failure" >&2
  exit 1
fi
if HOME="$tmp/home" DSH_HOME="$tmp/outside" bash "$ROOT/scripts/install.sh" --global >/dev/null 2>&1; then
  echo "expected unsafe DSH_HOME failure" >&2
  exit 1
fi
# Single-Skill install is supported independently.
mkdir -p "$tmp/only"
bash "$ROOT/scripts/install.sh" --project "$tmp/only" --skill ui-quality-audit
test -f "$tmp/only/.dsh/skills/ui-quality-audit/SKILL.md"
test ! -e "$tmp/only/.dsh/skills/frontend-engineering"
echo "Installer tests: PASS"
