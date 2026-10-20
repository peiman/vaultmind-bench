# Public benchmark harness

One scorer and one token counter for every system (Principle 7 — one source of truth).
Build and debug on a development set. Point the same commands at the held-out set
only after the freeze commit, once, and do not re-run to improve a number.

Runners see the question text and the section notes. `score.py` is the only
program that reads `expected`. Nothing here reads `keyphrase`, `keyphrases.tsv`,
or `evidence.tsv`.

## Command

From the repository root:

```sh
bash harness/run_all.sh \
  sets/devB \
  devB
```

`run_all.sh <set_dir> <out_dir>` runs every system, writes `versions.json`,
then `score.py`. A cheap agent check, before the full 50:

```sh
python3 harness/run_agent_rg.py \
  sets/devB /tmp/public-bench-agent-dry --max-questions 3
```

Unit tests:

```sh
python3 harness/test_harness.py
```

## What each system does

Section notes are the imported Markdown files that are not parent index notes.
A parent index is `<stem>.md` beside the directory `<stem>/`. `corpus.py` is
the only place that decides this. It does not open `queries.yaml`.

| system | file | run | `ranked` | `delivered_tokens` |
|---|---|---|---|---|
| `vm` | `run_vm.py` | Copy the vault to a temp dir (the gitignored SQLite index is left behind), `vaultmind index --embed`, then `vaultmind ask "<q>" --json` with no other ask flags. `XDG_DATA_HOME`, `XDG_STATE_HOME`, and `VAULTMIND_NO_SERVE=1` point at temp dirs. | `top_hits` ids, best first, parents included. A parent at position 1 leaves the next id at position 2. | Tokens of the title and body text in the JSON context pack. |
| `bm25` | `run_bm25.py` | In-memory SQLite FTS5 table `(title, body)`, tokenizer `unicode61`, `bm25()` with default column weights. The query is the question's alphanumeric words, each double-quoted, joined with `OR`. | Matching section ids, best first (`bm25()` ascending, then id). | Top 3 section texts. |
| `rg` | `run_rg.py` | Content words: lowercase, length at least 3, minus the stopword list in the file. For each word, `rg -i -c -F`. | Distinct words matched, then total line count, then path. Zero-match files are omitted. | Top 3 section texts. |
| `agent-rg` | `run_agent_rg.py` | One `claude -p` per question, model `claude-haiku-5-5`. The working directory contains only `<id>.md` section files and no labels. | Up to 3 file names from the JSON array in the reply, best first. | `usage.input_tokens` + `usage.cache_creation_input_tokens` + `usage.output_tokens`. A dev B probe showed `input_tokens` alone is the uncached remainder (41) while tool results land in `cache_creation_input_tokens`. `cache_read_input_tokens` is stored on the row and left out of the sum so the same context is not counted on every turn. `output_tokens` includes the final answer and any thinking tokens. The CLI does not split tool-result text out from the prompt. |
| `whole` | `run_whole.py` | No retrieval. The document is every section of the question's `doc`, path order. | `[]` | Token count of that document. `fits_200k` is true at 200,000 tokens or fewer. |
| `qmd` | `run_qmd.py` | Runs only if `qmd` is already on `PATH` or `npm install @tobilu/qmd` finishes in 45 seconds. Otherwise `qmd.skip` holds one line and the reason. | — | — |

`vm` uses the settings the release binary ships. No budget, excerpt, model, or search-limit flag is passed.

The agent command restricts tools with `--tools Grep,Glob,Read`. On this CLI, `--allowedTools` only pre-approves permissions; it does not remove other tools (`claude --help`). `--restricted` keeps Grep, Glob, and Read inside the working directory and ignores user and project settings, so this repo's instructions are not loaded. The run also passes `--permission-mode dontAsk`, `--permission-prompts none`, `--strict-mcp-config`, `--no-session-persistence`, and `--max-turns 15`. The prompt is the constant `PROMPT` in `run_agent_rg.py`:

```
Find the sections of these docs most likely to answer the question. Reply with ONLY a JSON array of up to 3 file names, best first.

Question: <question text>
```

## Tokens

`tokens.py` counts with tiktoken `cl100k_base` when `tiktoken` imports, otherwise `ceil(chars/4)`. Every JSONL row has `token_method` set to that name, and `scores.json` repeats it. `agent-rg` still records the method. Its `delivered_tokens` number is the Claude usage sum described above, not a `tokens.py` count of file text, and `delivered_tokens_are` says so.

`score.py` reads each `<system>.jsonl` and `queries.yaml`. A hit at k means the labelled section id occurs at rank ≤ k. Rank is 1-based. Ids that are not the label, including parent notes, still occupy a position. It writes `scores.md` and `scores.json`: Hit@1, Hit@3, mean and median delivered tokens, mean seconds, and a miss list per system.

## Versions

`versions.json` records the `vaultmind` version, `rg` version, Claude CLI version, model id, Python version, and the git SHA of the repository that contains the set.
