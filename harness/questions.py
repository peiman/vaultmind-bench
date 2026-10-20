"""Questions for a benchmark set.

`prompts` is what runners see: name, text, and the document id. Labels
(`expected`) are loaded only for the scorer. keyphrase is never loaded.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def load(set_dir: str | Path) -> list[dict]:
    """Full records. `expected` is for score.py only."""
    path = Path(set_dir) / "queries.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"{path} is not a YAML list of questions")
    out = []
    for q in data:
        expected = q.get("expected") or []
        if isinstance(expected, str):
            expected = [expected]
        out.append(
            {
                "name": q["name"],
                "text": q["text"],
                "doc": q.get("doc") or "",
                "expected": list(expected),
            }
        )
    return out


def prompts(set_dir: str | Path) -> list[dict]:
    """Runner view. No labels."""
    return [
        {"name": q["name"], "text": q["text"], "doc": q["doc"]}
        for q in load(set_dir)
    ]
