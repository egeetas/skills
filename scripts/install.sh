#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Install this repository's skills for Codex.

Usage:
  ./scripts/install.sh [--scope user|repo] [--target PATH] [--with-agents] [skill ...]
  ./scripts/install.sh --list

Scopes:
  user  Symlink skills into $HOME/.agents/skills (default).
  repo  Copy skills into TARGET/.agents/skills; --target is required.

Options:
  --with-agents  Also install the optional Codex subagent presets.

Examples:
  ./scripts/install.sh
  ./scripts/install.sh frontend-design test-and-fix-loop
  ./scripts/install.sh --scope repo --target /path/to/project --with-agents

Existing destinations are never overwritten.
USAGE
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
scope="user"
target=""
list_only="false"
with_agents="false"
requested=()

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
    --list)
      list_only="true"
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
      requested+=("$1")
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

if [[ ${#requested[@]} -eq 0 ]]; then
  requested=("${available[@]}")
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
