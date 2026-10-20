"""VaultMind ask, release binary, default settings.

Copies the set's vault to a temp directory, drops the rebuildable SQLite
index (it is gitignored and may belong to an older binary), then runs
`vaultmind index --embed` and `vaultmind ask "<q>" --json`. No ask flag
is set. XDG_DATA_HOME, XDG_STATE_HOME, and VAULTMIND_NO_SERVE isolate the run.

ranked is the top_hits ids in order, parents included, so a parent at
position 1 leaves the first section at position 2. delivered_tokens is
the token count of the text in the JSON context pack (titles and bodies).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import questions
import tokens


def _ignore_index(_directory: str, names: list[str]) -> set[str]:
    skip = set()
    for name in names:
        if name.startswith("index.db") or name == "fingerprint.txt":
            skip.add(name)
    return skip


def parse_stdout(text: str) -> dict:
    raw = text.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            return json.loads(raw[start : end + 1])
        raise


def _piece(item: dict) -> str:
    if not isinstance(item, dict):
        return ""
    frontmatter = item.get("frontmatter") or {}
    title = ""
    if isinstance(frontmatter, dict) and frontmatter.get("title"):
        title = str(frontmatter["title"])
    body = item.get("body") or ""
    if title and body:
        return f"{title}\n{body}"
    return body or title


def delivered_text(result: dict) -> str:
    """Text ask put in the JSON context pack. Empty when nothing was packed."""
    context = result.get("context") or {}
    if not isinstance(context, dict):
        return ""
    parts = []
    target = _piece(context.get("target") or {})
    if target:
        parts.append(target)
    for item in context.get("context") or []:
        text = _piece(item)
        if text:
            parts.append(text)
    return "\n\n".join(parts)


def parse_ask(payload: dict) -> tuple[list[str], str]:
    """Return (ranked ids, delivered text). Ranked is the full top_hits list."""
    if payload.get("status") not in (None, "ok"):
        errors = payload.get("errors") or payload
        raise SystemExit(f"vaultmind ask status {payload.get('status')}: {errors}")
    result = payload.get("result")
    if not isinstance(result, dict):
        raise SystemExit("vaultmind ask JSON has no result object")
    ranked = []
    for hit in result.get("top_hits") or []:
        if isinstance(hit, dict) and hit.get("id"):
            ranked.append(hit["id"])
    return ranked, delivered_text(result)


def vaultmind_version() -> str:
    proc = subprocess.run(["vaultmind", "--version"], capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "vaultmind --version failed")
    return (proc.stdout or proc.stderr).strip()


def prepare_vault(
    set_dir: Path, root: Path, name: str = "vault", xdg_root: Path | None = None
) -> tuple[Path, dict]:
    """Copy the set's vault under root, index and embed it, return (vault, env).

    One setup for every system that runs vaultmind (vm, agent-vm). xdg_root
    keeps the XDG dirs out of an agent's working directory.
    """
    vault = root / name
    xdg_data = (xdg_root or root) / "xdg-data"
    xdg_state = (xdg_root or root) / "xdg-state"
    xdg_data.mkdir()
    xdg_state.mkdir()
    shutil.copytree(set_dir / "vault", vault, ignore=_ignore_index)
    env = os.environ.copy()
    env["XDG_DATA_HOME"] = str(xdg_data)
    env["XDG_STATE_HOME"] = str(xdg_state)
    env["VAULTMIND_NO_SERVE"] = "1"
    print(f"vm index --embed {vault}", flush=True)
    indexed = subprocess.run(
        ["vaultmind", "index", "--embed", "--vault", str(vault)],
        env=env,
    )
    if indexed.returncode != 0:
        raise SystemExit(f"vaultmind index failed ({indexed.returncode})")
    return vault, env


def run(set_dir: Path, out_dir: Path) -> None:
    version = vaultmind_version()
    print(version, flush=True)
    prompts = questions.prompts(set_dir)
    with tempfile.TemporaryDirectory(prefix="public-bench-vm-") as tmp:
        vault, env = prepare_vault(set_dir, Path(tmp))
        rows = []
        for i, q in enumerate(prompts, 1):
            t0 = time.perf_counter()
            proc = subprocess.run(
                ["vaultmind", "ask", q["text"], "--vault", str(vault), "--json"],
                env=env,
                capture_output=True,
                text=True,
            )
            seconds = time.perf_counter() - t0
            if proc.returncode != 0:
                raise SystemExit(
                    f"vaultmind ask failed on {q['name']} ({proc.returncode}): "
                    f"{proc.stderr[-500:]}"
                )
            ranked, text = parse_ask(parse_stdout(proc.stdout))
            rows.append(
                {
                    "name": q["name"],
                    "ranked": ranked,
                    "delivered_tokens": tokens.count(text),
                    "delivered_tokens_are": "ask JSON context-pack title and body text",
                    "seconds": round(seconds, 3),
                    "vaultmind_version": version,
                }
            )
            print(f"vm {i}/{len(prompts)} {q['name']} {seconds:.1f}s", flush=True)
    tokens.write_jsonl(out_dir / "vm.jsonl", rows)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir))


if __name__ == "__main__":
    main(sys.argv[1:])
