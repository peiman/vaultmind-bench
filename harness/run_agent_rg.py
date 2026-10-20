"""An agent driving grep, one Claude Code run per question.

The working directory holds only the section files, named `<id>.md`, with
no labels. Tools are limited to Grep, Glob, and Read. `--allowedTools` on
this CLI is a permission allow-list, not a tool restriction; `--tools`
(from `claude --help`) is what limits the available set. Permission mode
`dontAsk` plus `--strict-mcp-config` keeps the run from prompting or
picking up other servers. `--restricted` confines those tools to the
working directory and ignores user and project settings.

delivered_tokens is taken from the CLI JSON usage object, which is a
session total (the same numbers as modelUsage). On this CLI,
usage.input_tokens is only the uncached remainder — a probe on dev B
reported 41 — while tool results land in cache_creation_input_tokens.
cache_read_input_tokens repeats that context on later turns, so it is not
added. output_tokens is added because the contract counts the final answer;
it also includes thinking tokens. The CLI does not split tool-result text
out from the prompt. The sum is not the harness token counter.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import corpus
import questions
import tokens

MODEL = "claude-haiku-5-5"
TOOLS = "Grep,Glob,Read"

# Fixed prompt. {question} is the only substitution.
PROMPT = (
    "Find the sections of these docs most likely to answer the question. "
    "Reply with ONLY a JSON array of up to 3 file names, best first.\n\n"
    "Question: {question}\n"
)


def parse_filenames(text: str) -> list[str]:
    """Pull the JSON array of file names out of the agent's reply."""
    if not text:
        return []
    start = text.find("[")
    end = text.rfind("]")
    if start < 0 or end <= start:
        return []
    try:
        arr = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return []
    if not isinstance(arr, list):
        return []
    names = []
    for item in arr:
        if not isinstance(item, str):
            continue
        base = os.path.basename(item.strip())
        if base.endswith(".md"):
            base = base[: -len(".md")]
        if base:
            names.append(base)
    return names


def ranked_ids(text: str, valid_ids: set[str]) -> list[str]:
    """Up to 3 known section ids, in the order the agent returned."""
    out = []
    seen = set()
    for name in parse_filenames(text):
        if name in valid_ids and name not in seen:
            out.append(name)
            seen.add(name)
        if len(out) == 3:
            break
    return out


DELIVERED_TOKENS_ARE = (
    "usage.input_tokens + usage.cache_creation_input_tokens + usage.output_tokens; "
    "cache_read_input_tokens excluded so repeated context is not counted again. "
    "Tool-result text is inside cache_creation, not split out. "
    "output_tokens includes the final answer and any thinking tokens."
)


def usage_counts(payload: dict) -> dict[str, int]:
    """Session usage fields the CLI reports. input_tokens must be present."""
    usage = payload.get("usage") or {}
    if not isinstance(usage, dict) or "input_tokens" not in usage:
        raise SystemExit(
            "claude JSON has no usage.input_tokens: " + json.dumps(list(payload))[:300]
        )
    if "output_tokens" not in usage:
        raise SystemExit(
            "claude JSON has no usage.output_tokens: " + json.dumps(list(payload))[:300]
        )

    def n(key: str) -> int:
        value = usage.get(key, 0)
        return int(value or 0)

    return {
        "input_tokens": n("input_tokens"),
        "cache_creation_input_tokens": n("cache_creation_input_tokens"),
        "cache_read_input_tokens": n("cache_read_input_tokens"),
        "output_tokens": n("output_tokens"),
    }


def delivered_tokens(payload: dict) -> int:
    """New input, including tool results, plus the model's output."""
    counts = usage_counts(payload)
    return (
        counts["input_tokens"]
        + counts["cache_creation_input_tokens"]
        + counts["output_tokens"]
    )


def model_id(payload: dict) -> str:
    usage = payload.get("modelUsage")
    if isinstance(usage, dict) and usage:
        return next(iter(usage))
    reported = payload.get("model")
    if isinstance(reported, str) and reported:
        return reported
    return MODEL


def result_text(payload: dict) -> str:
    result = payload.get("result")
    if isinstance(result, str):
        return result
    return ""


def claude_version() -> str:
    proc = subprocess.run(["claude", "--version"], capture_output=True, text=True)
    return (proc.stdout or proc.stderr).strip()


def write_corpus(directory: Path, notes: list) -> None:
    for note in notes:
        body = corpus.section_text(note) + "\n"
        (directory / f"{note.id}.md").write_text(body, encoding="utf-8")


def agent_command(prompt: str, tools: str, allowed: str) -> list[str]:
    """One headless Claude Code run. tools limits what exists; allowed is what runs."""
    return [
        "claude",
        "-p",
        prompt,
        "--model",
        MODEL,
        "--tools",
        tools,
        "--allowedTools",
        allowed,
        "--output-format",
        "json",
        "--permission-mode",
        "dontAsk",
        "--permission-prompts",
        "none",
        "--strict-mcp-config",
        "--restricted",
        "--no-session-persistence",
        "--max-turns",
        "15",
    ]


def run(set_dir: Path, out_dir: Path, max_questions: int | None) -> None:
    run_agent("agent-rg", set_dir, out_dir, max_questions, PROMPT, TOOLS, TOOLS)


def run_agent(
    system: str,
    set_dir: Path,
    out_dir: Path,
    max_questions: int | None,
    prompt: str,
    tools: str,
    allowed: str,
    prepare=None,
) -> None:
    """Shared by agent-rg and agent-vm. prepare(work) may add files and return an env."""
    version = claude_version()
    print(f"claude {version} model {MODEL}", flush=True)
    notes = corpus.sections(set_dir)
    valid = {n.id for n in notes}
    prompts = questions.prompts(set_dir)
    if max_questions is not None:
        prompts = prompts[:max_questions]
    with tempfile.TemporaryDirectory(prefix=f"public-bench-{system}-") as tmp:
        work = Path(tmp)
        write_corpus(work, notes)
        env = prepare(work) if prepare else None
        rows = []
        for i, q in enumerate(prompts, 1):
            t0 = time.perf_counter()
            proc = subprocess.run(
                agent_command(prompt.format(question=q["text"]), tools, allowed),
                cwd=work,
                env=env,
                capture_output=True,
                text=True,
            )
            seconds = time.perf_counter() - t0
            if proc.returncode != 0 and not proc.stdout.strip():
                raise SystemExit(
                    f"claude failed on {q['name']} ({proc.returncode}): {proc.stderr[-800:]}"
                )
            try:
                payload = json.loads(proc.stdout)
            except json.JSONDecodeError as exc:
                raise SystemExit(
                    f"claude JSON parse failed on {q['name']}: {exc}; "
                    f"stderr={proc.stderr[-400:]}"
                ) from exc
            if payload.get("is_error"):
                raise SystemExit(f"claude error on {q['name']}: {result_text(payload)[:400]}")
            ranked = ranked_ids(result_text(payload), valid)
            reported = model_id(payload)
            counts = usage_counts(payload)
            rows.append(
                {
                    "name": q["name"],
                    "ranked": ranked,
                    "delivered_tokens": delivered_tokens(payload),
                    "delivered_tokens_are": DELIVERED_TOKENS_ARE,
                    "usage_input_tokens": counts["input_tokens"],
                    "usage_cache_creation_input_tokens": counts["cache_creation_input_tokens"],
                    "usage_cache_read_input_tokens": counts["cache_read_input_tokens"],
                    "usage_output_tokens": counts["output_tokens"],
                    "seconds": round(seconds, 3),
                    "model": reported,
                    "claude_cli": version,
                }
            )
            print(
                f"{system} {i}/{len(prompts)} {q['name']} {seconds:.1f}s "
                f"ranked={len(ranked)}",
                flush=True,
            )
    tokens.write_jsonl(out_dir / f"{system}.jsonl", rows)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    parser.add_argument("--max-questions", type=int, default=None)
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir), args.max_questions)


if __name__ == "__main__":
    main(sys.argv[1:])
