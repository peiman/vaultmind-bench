#!/usr/bin/env bash
# Run every system on one set, then score them with the same scorer.
# Usage: bash run_all.sh <set_dir> <out_dir>
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: bash run_all.sh <set_dir> <out_dir>" >&2
  exit 2
fi

SET=$(cd "$1" && pwd)
mkdir -p "$2"
OUT=$(cd "$2" && pwd)
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE"

python3 run_bm25.py "$SET" "$OUT"
python3 run_rg.py "$SET" "$OUT"
python3 run_whole.py "$SET" "$OUT"
python3 run_qmd.py "$SET" "$OUT"
python3 run_vm.py "$SET" "$OUT"
python3 run_agent_rg.py "$SET" "$OUT"
python3 run_agent_vm.py "$SET" "$OUT"

python3 - "$SET" "$OUT" <<'PY'
import json, subprocess, sys
from pathlib import Path

set_dir, out = sys.argv[1:]

def capture(args):
    proc = subprocess.run(args, capture_output=True, text=True)
    text = (proc.stdout or proc.stderr).strip()
    return text

import importlib, sys as _s
_s.path.insert(0, ".")
model = importlib.import_module("run_agent_rg").MODEL
agent = Path(out) / "agent-rg.jsonl"
if agent.is_file():
    first = agent.read_text(encoding="utf-8").splitlines()
    if first:
        model = json.loads(first[0]).get("model") or model

rg = capture(["rg", "--version"]).splitlines()
versions = {
    "vaultmind": capture(["vaultmind", "--version"]),
    "rg": rg[0] if rg else "",
    "claude_cli": capture(["claude", "--version"]),
    "model_id": model,
    "python": capture(["python3", "--version"]),
    "harness_git_sha": capture(["git", "-C", set_dir, "rev-parse", "HEAD"]),
}
Path(out, "versions.json").write_text(json.dumps(versions, indent=2) + "\n", encoding="utf-8")
print(json.dumps(versions, indent=2))
PY

python3 score.py "$SET" "$OUT"
