"""QMD, only when its published package installs and the binary runs.

`npm` package `qmd` is an unrelated 2016 placeholder. The search tool is
`@tobilu/qmd`. This runner spends one 45-second attempt on
`npm install @tobilu/qmd` when `qmd` is not already on PATH. If that does
not produce a working binary, it writes one line to `qmd.skip` and exits 0.

`ranked_from_payload` is the parser the runner would use. It is covered by
the unit test. The install attempt on this machine does not reach it when
the package does not come up in time.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

INSTALL_SECONDS = 45


def ranked_from_payload(payload, valid_ids: set[str]) -> list[str]:
    """Section ids from a qmd --json payload, best first."""
    if isinstance(payload, dict):
        rows = payload.get("results") or payload.get("hits") or []
    elif isinstance(payload, list):
        rows = payload
    else:
        return []
    out = []
    seen = set()
    for row in rows:
        if isinstance(row, str):
            name = row
        elif isinstance(row, dict):
            name = str(
                row.get("file")
                or row.get("path")
                or row.get("displayPath")
                or row.get("docid")
                or ""
            )
        else:
            continue
        base = os.path.basename(name.strip())
        if base.endswith(".md"):
            base = base[: -len(".md")]
        if base in valid_ids and base not in seen:
            out.append(base)
            seen.add(base)
    return out


def _version(binary: str) -> str:
    try:
        proc = subprocess.run(
            [binary, "--version"], capture_output=True, text=True, timeout=20
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    if proc.returncode != 0:
        return ""
    lines = (proc.stdout or proc.stderr).strip().splitlines()
    return lines[0] if lines else ""


def attempt() -> tuple[str, str]:
    """Return (binary, "") or ("", one-line reason)."""
    found = shutil.which("qmd")
    if found:
        version = _version(found)
        if version:
            return found, ""
        return "", f"qmd on PATH at {found} did not answer --version. Not run."
    with tempfile.TemporaryDirectory(prefix="public-bench-qmd-") as tmp:
        try:
            proc = subprocess.run(
                ["npm", "install", "--prefix", tmp, "@tobilu/qmd"],
                capture_output=True,
                text=True,
                timeout=INSTALL_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return "", (
                "npm install @tobilu/qmd did not finish in 45s "
                "(node-llama-cpp native build). Not run."
            )
        except FileNotFoundError:
            return "", "npm is not installed and qmd is not on PATH. Not run."
        binary = str(Path(tmp) / "node_modules" / ".bin" / "qmd")
        if proc.returncode != 0 or not Path(binary).is_file():
            tail = (proc.stderr or proc.stdout or "").strip().splitlines()
            detail = tail[-1] if tail else f"exit {proc.returncode}"
            return "", f"npm install @tobilu/qmd failed ({detail}). Not run."
        version = _version(binary)
        if not version:
            return "", "npm install @tobilu/qmd produced a binary that did not run. Not run."
        # The prefix is deleted with the temp dir. A package this heavy is
        # not given a second, durable install in this short attempt.
        return "", (
            f"@tobilu/qmd {version} installed only into a temp prefix and is "
            "not on PATH. Not run."
        )


def run(out_dir: Path) -> None:
    binary, reason = attempt()
    if reason or not binary:
        text = reason or "qmd did not install. Not run."
        (out_dir / "qmd.skip").write_text(text + "\n", encoding="utf-8")
        print(f"qmd skip: {text}", flush=True)
        return
    # On PATH. Still not invoked here: pointing qmd at the corpus writes an
    # index in the user's qmd home, and this short attempt does not do that.
    version = _version(binary)
    text = (
        f"qmd is on PATH ({binary}, {version}) but was not run: "
        "a short attempt has no isolated index directory. Not run."
    )
    (out_dir / "qmd.skip").write_text(text + "\n", encoding="utf-8")
    print(f"qmd skip: {text}", flush=True)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    run(out)


if __name__ == "__main__":
    main()
