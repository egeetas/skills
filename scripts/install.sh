#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Install this repository's skills for Codex.

Usage:
  ./scripts/install.sh [--scope user|repo] [--target PATH] [--with-agents]
                       [--pack NAME ...] [--all] [skill ...]
  ./scripts/install.sh --list
  ./scripts/install.sh --list-packs

Selection:
  No selection   Install the core-development pack.
  --pack NAME    Install a named pack; repeatable and combinable with skill names.
  --all          Install every skill; cannot be combined with packs or skill names.
  skill          Install an individual skill by name.

Scopes:
  user  Symlink skills into $HOME/.agents/skills (default).
  repo  Copy skills into TARGET/.agents/skills; --target is required.

Options:
  --with-agents  Also install the optional Codex subagent presets.
  --list         List available skills and exit.
  --list-packs   List packs and their skills, then exit.

Examples:
  ./scripts/install.sh
  ./scripts/install.sh --pack frontend-mobile --pack security-operations
  ./scripts/install.sh frontend-design test-and-fix-loop
  ./scripts/install.sh --all --with-agents
  ./scripts/install.sh --scope repo --target /path/to/project --pack core-development

Existing destinations are never overwritten.
USAGE
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
scope="user"
target=""
list_only="false"
list_packs_only="false"
with_agents="false"
install_all="false"
requested=()
requested_packs=()

append_unique() {
  local candidate="$1"
  local present
  if [[ ${#requested[@]} -gt 0 ]]; then
    for present in "${requested[@]}"; do
      [[ "$present" == "$candidate" ]] && return 0
    done
  fi
  requested+=("$candidate")
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope)
      [[ $# -ge 2 ]] || { echo "Missing value for --scope" >&2; exit 2; }
      scope="$2"
      shift 2
      ;;
    --target)
      [[ $# -ge 2 ]] || { echo "Missing value for --target" >&2; exit 2; }
      target="$2"
      shift 2
      ;;
    --pack)
      [[ $# -ge 2 ]] || { echo "Missing value for --pack" >&2; exit 2; }
      requested_packs+=("$2")
      shift 2
      ;;
    --all)
      install_all="true"
      shift
      ;;
    --list)
      list_only="true"
      shift
      ;;
    --list-packs)
      list_packs_only="true"
      shift
      ;;
    --with-agents)
      with_agents="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      append_unique "$1"
      shift
      ;;
  esac
done

available=()
for entrypoint in "$repo_root"/skills/*/SKILL.md; do
  [[ -f "$entrypoint" ]] || continue
  available+=("$(basename "$(dirname "$entrypoint")")")
done

if [[ "$list_only" == "true" ]]; then
  printf '%s\n' "${available[@]}"
  exit 0
fi

if [[ "$list_packs_only" == "true" ]]; then
  for pack_file in "$repo_root"/packs/*.txt; do
    [[ -f "$pack_file" ]] || continue
    pack_name="$(basename "$pack_file" .txt)"
    printf '%s:' "$pack_name"
    while IFS= read -r skill || [[ -n "$skill" ]]; do
      [[ -z "$skill" || "$skill" == \#* ]] && continue
      printf ' %s' "$skill"
    done < "$pack_file"
    printf '\n'
  done
  exit 0
fi

if [[ "$install_all" == "true" && (${#requested[@]} -gt 0 || ${#requested_packs[@]} -gt 0) ]]; then
  echo "--all cannot be combined with --pack or individual skill names" >&2
  exit 2
fi

if [[ "$install_all" == "true" ]]; then
  requested=("${available[@]}")
else
  if [[ ${#requested[@]} -eq 0 && ${#requested_packs[@]} -eq 0 ]]; then
    requested_packs=("core-development")
  fi
  for pack_name in "${requested_packs[@]}"; do
    pack_file="$repo_root/packs/$pack_name.txt"
    [[ -f "$pack_file" ]] || { echo "Unknown pack: $pack_name" >&2; exit 2; }
    while IFS= read -r skill || [[ -n "$skill" ]]; do
      [[ -z "$skill" || "$skill" == \#* ]] && continue
      append_unique "$skill"
    done < "$pack_file"
  done
fi

case "$scope" in
  user)
    if [[ -n "$target" ]]; then
      destination_root="$target"
    else
      destination_root="$HOME/.agents/skills"
    fi
    install_mode="link"
    agent_destination_root="$HOME/.codex/agents"
    ;;
  repo)
    [[ -n "$target" ]] || { echo "--target is required for repo scope" >&2; exit 2; }
    [[ -d "$target" ]] || { echo "Target directory does not exist: $target" >&2; exit 2; }
    target="$(cd "$target" && pwd)"
    destination_root="$target/.agents/skills"
    install_mode="copy"
    agent_destination_root="$target/.codex/agents"
    ;;
  *)
    echo "Scope must be 'user' or 'repo': $scope" >&2
    exit 2
    ;;
esac

mkdir -p "$destination_root"
conflicts=0
installed=0

for name in "${requested[@]}"; do
  source_dir="$repo_root/skills/$name"
  destination="$destination_root/$name"

  if [[ ! "$name" =~ ^[a-z0-9-]+$ ]] || [[ ! -f "$source_dir/SKILL.md" ]]; then
    echo "Unknown skill: $name" >&2
    conflicts=$((conflicts + 1))
    continue
  fi

  if [[ -e "$destination" || -L "$destination" ]]; then
    if [[ "$install_mode" == "link" && -L "$destination" ]]; then
      current_target="$(readlink "$destination")"
      if [[ "$current_target" == "$source_dir" ]]; then
        echo "Already installed: $name"
        continue
      fi
      legacy_source="$repo_root/$name"
      if [[ "$current_target" == "$legacy_source" ]]; then
        ln -sfn "$source_dir" "$destination"
        echo "Migrated: $name -> $destination"
        installed=$((installed + 1))
        continue
      fi
    fi
    echo "Conflict, not overwritten: $destination" >&2
    conflicts=$((conflicts + 1))
    continue
  fi

  if [[ "$install_mode" == "link" ]]; then
    ln -s "$source_dir" "$destination"
  else
    cp -R "$source_dir" "$destination"
  fi
  echo "Installed: $name -> $destination"
  installed=$((installed + 1))
done

if [[ "$with_agents" == "true" ]]; then
  mkdir -p "$agent_destination_root"
  for source_agent in "$repo_root"/agent-presets/*.toml; do
    [[ -f "$source_agent" ]] || continue
    agent_name="$(basename "$source_agent")"
    agent_destination="$agent_destination_root/$agent_name"

    if [[ -e "$agent_destination" || -L "$agent_destination" ]]; then
      if [[ "$install_mode" == "link" && -L "$agent_destination" ]] && \
        [[ "$(readlink "$agent_destination")" == "$source_agent" ]]; then
        echo "Already installed agent: ${agent_name%.toml}"
        continue
      fi
      echo "Conflict, not overwritten: $agent_destination" >&2
      conflicts=$((conflicts + 1))
      continue
    fi

    if [[ "$install_mode" == "link" ]]; then
      ln -s "$source_agent" "$agent_destination"
    else
      cp "$source_agent" "$agent_destination"
    fi
    echo "Installed agent: ${agent_name%.toml} -> $agent_destination"
    installed=$((installed + 1))
  done
fi

if [[ "$install_mode" == "copy" ]]; then
  mkdir -p "$destination_root/LICENSES"
  cp -R "$repo_root/LICENSES/." "$destination_root/LICENSES/"
  cp "$repo_root/THIRD_PARTY_NOTICES.md" "$destination_root/THIRD_PARTY_NOTICES.md"
fi

echo "Completed: $installed installed, $conflicts conflicts"
if [[ $conflicts -gt 0 ]]; then
  exit 3
fi
