"""One token counter for every system (Principle 7 — one source of truth).

cl100k_base via tiktoken when that package imports, otherwise ceil(chars/4).
The method name is written onto every results row.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

_encoder = None
try:
    import tiktoken

    _encoder = tiktoken.get_encoding("cl100k_base")
    METHOD = "tiktoken-cl100k_base"
except Exception:
    METHOD = "ceil(chars/4)"


def count(text: str) -> int:
    """Token count of text. Empty text is 0."""
    if not text:
        return 0
    if _encoder is not None:
        return len(_encoder.encode(text))
    return math.ceil(len(text) / 4)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    """Write one JSON object per line. Every row records the token method."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            out = dict(row)
            out["token_method"] = METHOD
            fh.write(json.dumps(out, ensure_ascii=False) + "\n")
