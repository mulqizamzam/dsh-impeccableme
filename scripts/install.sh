#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
SOURCE_ROOT="$(cd -- "$SCRIPT_DIR/../.dsh/skills" && pwd -P)"
MODE=""; TARGET=""; SELECTED_SKILL=""; REPLACE=0
usage(){ echo "Usage: $0 --project PATH | --global [--skill NAME] [--replace]"; }
while (($#)); do case "$1" in
 --project) [[ -n "${2:-}" ]] || { usage >&2; exit 2; }; MODE=project; TARGET=$2; shift 2;;
 --global) MODE=global; shift;;
 --skill) [[ -n "${2:-}" ]] || { usage >&2; exit 2; }; SELECTED_SKILL=$2; shift 2;;
 --replace) REPLACE=1; shift;;
 -h|--help) usage; exit 0;;
 *) usage >&2; exit 2;; esac; done
[[ -n "$MODE" ]] || { usage >&2; exit 2; }
if [[ -n "$SELECTED_SKILL" && ! "$SELECTED_SKILL" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then echo "error: invalid skill slug" >&2; exit 2; fi
if [[ "$MODE" == project ]]; then
 [[ -d "$TARGET" ]] || { echo "error: project path must exist" >&2; exit 2; }
 DEST_ROOT="$TARGET/.dsh/skills"; mkdir -p -- "$DEST_ROOT"; DEST_ROOT="$(cd -- "$DEST_ROOT" && pwd -P)"
else
 HOME_ROOT="$(cd -- "$HOME" && pwd -P)"; DSH_ROOT="${DSH_HOME:-$HOME/.dsh}"
 ancestor="$DSH_ROOT"; while [[ ! -d "$ancestor" ]]; do parent="$(dirname -- "$ancestor")"; [[ "$parent" != "$ancestor" ]] || exit 2; ancestor="$parent"; done
 ancestor_real="$(cd -- "$ancestor" && pwd -P)"; case "$ancestor_real" in "$HOME_ROOT"|"$HOME_ROOT"/*) ;; *) echo "error: DSH_HOME outside HOME" >&2; exit 2;; esac
 [[ ! -L "$DSH_ROOT/skills" ]] || { echo "error: refusing global Skill-root symlink" >&2; exit 2; }
 mkdir -p -- "$DSH_ROOT/skills"; DEST_ROOT="$(cd -- "$DSH_ROOT/skills" && pwd -P)"
fi
[[ "$SOURCE_ROOT" != "$DEST_ROOT" ]] || { echo "error: source and destination match" >&2; exit 2; }
shopt -s nullglob
if [[ -n "$SELECTED_SKILL" ]]; then SKILL_DIRS=("$SOURCE_ROOT/$SELECTED_SKILL"); else SKILL_DIRS=("$SOURCE_ROOT"/*); fi
shopt -u nullglob
((${#SKILL_DIRS[@]} > 0)) || { echo "error: no Skills found" >&2; exit 1; }
for skill in "${SKILL_DIRS[@]}"; do
 [[ -d "$skill" && -f "$skill/SKILL.md" ]] || { echo "error: invalid Skill: $skill" >&2; exit 1; }
 dest="$DEST_ROOT/$(basename -- "$skill")"
 if [[ -e "$dest" && "$REPLACE" -ne 1 ]]; then echo "error: destination exists: $dest (use --replace after review)" >&2; exit 1; fi
done
for skill in "${SKILL_DIRS[@]}"; do dest="$DEST_ROOT/$(basename -- "$skill")"; temp="$DEST_ROOT/.install-$(basename -- "$skill")-$$"; rm -rf -- "$temp"; cp -R -- "$skill" "$temp"; if [[ -e "$dest" ]]; then old="$DEST_ROOT/.previous-$(basename -- "$skill")-$$"; mv -- "$dest" "$old"; if mv -- "$temp" "$dest"; then rm -rf -- "$old"; else mv -- "$old" "$dest"; exit 1; fi; else mv -- "$temp" "$dest"; fi; echo "installed: $dest"; done
echo "Done. Restart or refresh DSH if its Skill catalog has not updated."
