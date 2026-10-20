"""Whole-document baseline.

For each question, count tokens of the parent document named by `doc`
(all of that document's section texts, path order). No labels are read.
ranked is empty. fits_200k is true when the count is at most 200_000.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import corpus
import questions
import tokens

CONTEXT_LIMIT = 200_000


def fits_200k(n_tokens: int) -> bool:
    return n_tokens <= CONTEXT_LIMIT


def run(set_dir: Path, out_dir: Path) -> None:
    notes = corpus.sections(set_dir)
    by_doc: dict[str, list] = {}
    for note in notes:
        by_doc.setdefault(note.parent_doc_id, []).append(note)
    texts = {doc: corpus.document_text(group) for doc, group in by_doc.items()}
    rows = []
    for i, q in enumerate(questions.prompts(set_dir), 1):
        if q["doc"] not in texts:
            known = ", ".join(sorted(texts))
            raise SystemExit(f"{q['name']}: doc {q['doc']!r} is not a parent document ({known})")
        t0 = time.perf_counter()
        n_tokens = tokens.count(texts[q["doc"]])
        seconds = time.perf_counter() - t0
        rows.append(
            {
                "name": q["name"],
                "ranked": [],
                "delivered_tokens": n_tokens,
                "delivered_tokens_are": "whole parent document",
                "fits_200k": fits_200k(n_tokens),
                "seconds": round(seconds, 3),
            }
        )
        print(f"whole {i} {q['name']} tokens={n_tokens} fits={fits_200k(n_tokens)}", flush=True)
    tokens.write_jsonl(out_dir / "whole.jsonl", rows)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir))


if __name__ == "__main__":
    main(sys.argv[1:])
