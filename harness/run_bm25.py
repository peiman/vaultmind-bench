"""BM25 over section title and body, SQLite FTS5, default bm25() weights.

Query: the question's alphanumeric words, each double-quoted, joined with OR.
Tokenizer: unicode61. Better matches are the more negative bm25() scores.
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
import time
from pathlib import Path

import corpus
import questions
import tokens

_WORD = re.compile(r"[0-9A-Za-z]+")


def fts_query(text: str) -> str:
    words = _WORD.findall(text)
    if not words:
        return ""
    return " OR ".join(f'"{word}"' for word in words)


def rank(notes: list, query_text: str) -> list[str]:
    """Section ids, best first. Notes need id, title, body."""
    query = fts_query(query_text)
    if not query or not notes:
        return []
    con = sqlite3.connect(":memory:")
    try:
        con.execute(
            "CREATE VIRTUAL TABLE docs USING fts5("
            "id UNINDEXED, title, body, tokenize='unicode61')"
        )
        con.executemany(
            "INSERT INTO docs(id, title, body) VALUES (?, ?, ?)",
            [(n.id, n.title, n.body) for n in notes],
        )
        rows = con.execute(
            "SELECT id FROM docs WHERE docs MATCH ? ORDER BY bm25(docs), id",
            (query,),
        ).fetchall()
    finally:
        con.close()
    return [row[0] for row in rows]


def delivered_tokens(notes_by_id: dict, ranked: list[str]) -> int:
    return sum(tokens.count(corpus.section_text(notes_by_id[i])) for i in ranked[:3])


def run(set_dir: Path, out_dir: Path) -> None:
    notes = corpus.sections(set_dir)
    by_id = {n.id: n for n in notes}
    rows = []
    for i, q in enumerate(questions.prompts(set_dir), 1):
        t0 = time.perf_counter()
        ranked = rank(notes, q["text"])
        seconds = time.perf_counter() - t0
        rows.append(
            {
                "name": q["name"],
                "ranked": ranked,
                "delivered_tokens": delivered_tokens(by_id, ranked),
                "delivered_tokens_are": "top-3 section texts",
                "seconds": round(seconds, 3),
            }
        )
        print(f"bm25 {i} {q['name']} {seconds:.2f}s", flush=True)
    tokens.write_jsonl(out_dir / "bm25.jsonl", rows)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir))


if __name__ == "__main__":
    main(sys.argv[1:])
