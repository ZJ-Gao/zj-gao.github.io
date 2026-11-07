#!/usr/bin/env bash
# Update Google Scholar citation counts from this Mac, then optionally commit and push.
# Usage: bin/update-citations-local.sh
# A home network is blocked by Google Scholar far less often than GitHub's servers.
set -euo pipefail

cd "$(dirname "$0")/.."
VENV=.venv-citations

if [ ! -x "$VENV/bin/python" ]; then
  echo "First run: setting up a small Python environment in $VENV ..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q --upgrade pip
  "$VENV/bin/pip" install -q scholarly PyYAML "bibtexparser<2"
fi

"$VENV/bin/python" -u bin/update_scholar_citations.py

if git diff --quiet -- _data/citations.yml; then
  echo "Nothing to commit."
  exit 0
fi

branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" != "master" ]; then
  echo "You are on branch '$branch', not master: left uncommitted. The local preview already shows the new numbers."
  exit 0
fi

answer=""
if [ -t 0 ]; then
  read -r -p "Commit and push the new counts so the live site updates? [y/N] " answer || answer=""
else
  echo "No terminal to ask in (for example when run with ! inside Claude Code): treating it as no."
fi
if [[ "$answer" =~ ^[Yy]$ ]]; then
  git add _data/citations.yml
  git commit -m "Update Google Scholar citations"
  git push
  echo "Pushed. The live site rebuilds in a few minutes."
else
  echo "Left uncommitted. The local preview already shows the new numbers."
fi
