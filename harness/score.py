"""One scorer for every system.

A hit at k means the labelled section id is at rank <= k in `ranked`.
Parents and any other ids in that list occupy positions. Rank is 1-based.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

import questions
import tokens

SYSTEM_ORDER = ["vm", "bm25", "rg", "agent-rg", "agent-vm", "whole", "qmd"]


def label_rank(ranked: list[str], expected: list[str]) -> int | None:
    """1-based rank of the first labelled id, or None when it is absent."""
    wanted = set(expected)
    for index, note_id in enumerate(ranked, 1):
        if note_id in wanted:
            return index
    return None


def hit(rank: int | None, k: int) -> bool:
    return rank is not None and rank <= k


def score_rows(labelled: list[dict], rows: list[dict]) -> dict:
    by_name = {row["name"]: row for row in rows}
    hit1 = 0
    hit3 = 0
    tokens_list = []
    seconds = []
    misses = []
    fits = []
    n = len(labelled)
    for question in labelled:
        row = by_name.get(question["name"])
        if row is None:
            misses.append({"name": question["name"], "rank": None, "expected": question["expected"]})
            continue
        rank = label_rank(list(row.get("ranked") or []), question["expected"])
        if hit(rank, 1):
            hit1 += 1
        if hit(rank, 3):
            hit3 += 1
        else:
            misses.append(
                {
                    "name": question["name"],
                    "rank": rank,
                    "expected": question["expected"],
                }
            )
        tokens_list.append(int(row["delivered_tokens"]))
        seconds.append(float(row["seconds"]))
        if "fits_200k" in row:
            fits.append(bool(row["fits_200k"]))
    present = len(tokens_list)
    result = {
        "n": n,
        "scored": present,
        "hit_at_1": {"hits": hit1, "n": n},
        "hit_at_3": {"hits": hit3, "n": n},
        "delivered_tokens": {
            "mean": round(statistics.fmean(tokens_list), 1) if tokens_list else None,
            "median": statistics.median(tokens_list) if tokens_list else None,
        },
        "seconds_mean": round(statistics.fmean(seconds), 3) if seconds else None,
        "misses": misses,
    }
    if fits:
        result["fits_200k"] = {"fits": sum(fits), "n": len(fits)}
    return result


def load_system(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def systems(out_dir: Path) -> list[tuple[str, list[dict]]]:
    found = {}
    for path in sorted(out_dir.glob("*.jsonl")):
        found[path.stem] = load_system(path)
    names = [name for name in SYSTEM_ORDER if name in found]
    names.extend(name for name in sorted(found) if name not in names)
    return [(name, found[name]) for name in names]


def render_md(set_dir: Path, table: dict) -> str:
    lines = [
        "# Scores",
        "",
        f"Set: `{set_dir}`",
        "",
        f"Token method: `{table['token_method']}`",
        "",
        "| system | Hit@1 | Hit@3 | mean tokens | median tokens | mean seconds |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, row in table["systems"].items():
        h1 = row["hit_at_1"]
        h3 = row["hit_at_3"]
        delivered = row["delivered_tokens"]
        lines.append(
            f"| {name} | {h1['hits']}/{h1['n']} | {h3['hits']}/{h3['n']} | "
            f"{delivered['mean']} | {delivered['median']} | {row['seconds_mean']} |"
        )
    lines.append("")
    for name, row in table["systems"].items():
        if "fits_200k" in row:
            fits = row["fits_200k"]
            lines.append(f"{name} fits in 200k tokens: {fits['fits']}/{fits['n']}")
            lines.append("")
    lines.append("## Misses")
    lines.append("")
    lines.append("A miss is a question whose labelled section is not at rank 3 or better.")
    lines.append("Rank is 1-based in `ranked`; empty means the id was not in the list.")
    lines.append("")
    for name, row in table["systems"].items():
        lines.append(f"### {name}")
        lines.append("")
        if not row["misses"]:
            lines.append("None.")
            lines.append("")
            continue
        for miss in row["misses"]:
            where = "absent" if miss["rank"] is None else f"rank {miss['rank']}"
            expected = ", ".join(miss["expected"])
            lines.append(f"- `{miss['name']}` {where} (expected `{expected}`)")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def score(set_dir: Path, out_dir: Path) -> dict:
    labelled = questions.load(set_dir)
    table = {"token_method": tokens.METHOD, "set": str(set_dir), "systems": {}}
    for name, rows in systems(out_dir):
        table["systems"][name] = score_rows(labelled, rows)
    text = render_md(set_dir, table)
    (out_dir / "scores.md").write_text(text, encoding="utf-8")
    (out_dir / "scores.json").write_text(json.dumps(table, indent=2) + "\n", encoding="utf-8")
    print(text, end="")
    return table


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args(argv)
    score(Path(args.set_dir), Path(args.out_dir))


if __name__ == "__main__":
    main(sys.argv[1:])
