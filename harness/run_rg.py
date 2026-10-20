"""Ripgrep over section files.

Content words: lowercase alphanumeric tokens of length >= 3, minus the
stopword list below. For each word, `rg -i -c -F`. Rank by distinct words
matched (desc), total line-count (desc), path (asc). Files with no match
are left out of the ranking.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

import corpus
import questions
import tokens

# Fixed English stopword list. Tokens are alphanumeric, so contractions
# are the pieces left after the apostrophe is dropped ("don't" -> don, t).
STOPWORDS = frozenset(
    """
    a about above after again against all am an and any are aren aren't as at be
    because been before being below between both but by can cannot could couldn
    couldn't did didn didn't do does doesn doesn't doing don don't down during
    each few for from further had hadn hadn't has hasn hasn't have haven haven't
    having he her here hers herself him himself his how i if in into is isn
    isn't it its itself let's me more most my myself no nor not of off on once
    only or other ought our ours ourselves out over own same she should shouldn
    shouldn't so some such than that the their theirs them themselves then there
    these they this those through to too under until up very was wasn wasn't we
    were weren weren't what when where which while who whom why with won't
    would wouldn wouldn't you your yours yourself yourselves
    """.split()
)

_WORD = re.compile(r"[0-9A-Za-z]+")


def content_words(text: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for word in _WORD.findall(text.lower()):
        if len(word) < 3 or word in STOPWORDS or word in seen:
            continue
        seen.add(word)
        out.append(word)
    return out


def rank_counts(counts: dict[str, dict[str, int]], paths: dict[str, str]) -> list[str]:
    """counts[id][word] = matching-line count from rg -c. Best id first."""
    scored = []
    for note_id, per_word in counts.items():
        distinct = sum(1 for n in per_word.values() if n > 0)
        if distinct == 0:
            continue
        total = sum(per_word.values())
        scored.append((-distinct, -total, paths[note_id], note_id))
    scored.sort()
    return [note_id for _d, _t, _p, note_id in scored]


def rg_counts(word: str, files: list[Path]) -> dict[str, int]:
    """Map file path -> matching line count. Missing files mean zero."""
    if not files:
        return {}
    proc = subprocess.run(
        ["rg", "-i", "-c", "-F", "--", word, *[str(p) for p in files]],
        capture_output=True,
        text=True,
    )
    if proc.returncode not in (0, 1):
        raise SystemExit(f"rg failed ({proc.returncode}): {proc.stderr[:400]}")
    counts: dict[str, int] = {}
    for line in proc.stdout.splitlines():
        path, _, raw = line.rpartition(":")
        if not path:
            continue
        try:
            counts[path] = int(raw)
        except ValueError:
            continue
    return counts


def rank(notes: list, query_text: str) -> list[str]:
    words = content_words(query_text)
    paths = {n.id: str(n.path) for n in notes}
    files = [n.path for n in notes]
    by_path = {str(n.path): n.id for n in notes}
    counts = {n.id: {word: 0 for word in words} for n in notes}
    for word in words:
        for path, n in rg_counts(word, files).items():
            note_id = by_path.get(path)
            if note_id is not None:
                counts[note_id][word] = n
    return rank_counts(counts, paths)


def rg_version() -> str:
    proc = subprocess.run(["rg", "--version"], capture_output=True, text=True)
    line = (proc.stdout or proc.stderr).splitlines()
    return line[0].strip() if line else ""


def run(set_dir: Path, out_dir: Path) -> None:
    print(rg_version(), flush=True)
    notes = corpus.sections(set_dir)
    by_id = {n.id: n for n in notes}
    rows = []
    for i, q in enumerate(questions.prompts(set_dir), 1):
        t0 = time.perf_counter()
        ranked = rank(notes, q["text"])
        seconds = time.perf_counter() - t0
        delivered = sum(tokens.count(corpus.section_text(by_id[n])) for n in ranked[:3])
        rows.append(
            {
                "name": q["name"],
                "ranked": ranked,
                "delivered_tokens": delivered,
                "delivered_tokens_are": "top-3 section texts",
                "seconds": round(seconds, 3),
            }
        )
        print(f"rg {i} {q['name']} {seconds:.2f}s", flush=True)
    tokens.write_jsonl(out_dir / "rg.jsonl", rows)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir))


if __name__ == "__main__":
    main(sys.argv[1:])
