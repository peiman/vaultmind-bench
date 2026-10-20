# Method

## Question and unit

When a coding agent needs an answer that lives in a project's long docs, which
retrieval puts the right section in front of it, and at what token cost?

The unit is one imported **section note**. Each question is answered by exactly
one section. A hit on the document's parent note, or on another section of the
right document, is a miss.

## Sets

Both sets were built the same way: six long public technical documents imported
with `vaultmind import` (one page, converted to Markdown, split into section notes
when longer than 32,768 characters), then 50 natural agent-style questions written
by reading the imported files. Each label has a verbatim keyphrase that occurs in
exactly one section (`validate.py` checks this with string matching only).

- **Dev B** (development): Redis Cluster specification, Kubernetes pod lifecycle,
  nginx core module, RFC 9111, git-config, Python `logging`. Used to build and debug
  the harness.
- **Held-out** (judge): RFC 9113, Python `subprocess`, Kubernetes Deployments, Cargo
  configuration, MDN CORS, GitHub Actions workflow syntax. Frozen on 2026-10-16
  before any system ran on it. The only VaultMind commands that ever touched it
  before the run were `init` and `import`, with embedding off (see its README).

## Systems

Every system sees the same section files and only the question text.

| id | how it runs |
|---|---|
| `vm` | VaultMind v0.10.15 release binary (ORT, BGE-M3): `index --embed`, then `ask "<q>" --json` with default settings |
| `bm25` | SQLite FTS5 `bm25()` over (title, body), unicode61 tokenizer, the question's words OR-ed |
| `rg` | content words of the question; `rg -i -c -F` per word; rank by distinct words matched, then total matches |
| `agent-rg` | `claude -p` with `claude-haiku-5-5`, tools limited to Grep, Glob and Read in a directory holding only the section files; asked for up to 3 file names, best first |
| `agent-vm` | the same agent and prompt, plus Bash allowed only for `vaultmind ask` over an indexed copy of the docs; the prompt adds one sentence naming the command |
| `whole` | no ranking; the token count of the whole document |

Exact prompts and flags are in `harness/run_agent_rg.py` and `harness/run_agent_vm.py`.

## Metric and scorer

Hit@1 and Hit@3 on the labelled section; mean tokens delivered per answer; mean
seconds. Every system writes one JSONL row per question with its ranked section
ids. **One scorer** (`harness/score.py`) scores all of them; no system is scored by
its own tool. Tokens: tiktoken `cl100k_base` over delivered text (top-3 sections
for bm25 and rg; the delivered context for vm). For the agents, the session's new
input tokens plus cache-creation tokens (where tool results land) plus output tokens,
as reported by the CLI; repeated cache reads are excluded.

## Freeze and the single run

The harness was built and debugged on dev B only. It was then frozen (one commit
recording the harness, versions, model id and prompts), and run **once** on the
held-out set on 2026-10-20. No system was changed after seeing held-out results.

Two changes were made on dev B before the freeze, both recorded before the
held-out run: `agent-vm` was added, and both agents moved from Haiku 4.5 to the
current Haiku 5.5 (an older baseline model would flatter VaultMind).

## Pre-registered claims and their outcome

Fixed before the held-out run. We committed to publishing every number whatever
the outcome.

| claim | condition on the held-out set | measured | held? |
|---|---|---|---|
| 1 | VaultMind alone beats the better of ripgrep and agent+grep by ≥ 10 points Hit@3 | 45 vs 44 (+2 points) | no |
| 2 | agent+VaultMind within 1 question of agent+grep on Hit@3, at ≤ 60% of its tokens | 49 vs 44; 73% of the tokens | no (tokens) |
| 3 | agent+VaultMind beats agent+grep by ≥ 5 questions Hit@1, Hit@3 no worse | +4 questions | no |

Claim 3 was formed from a dev B observation (agent+VaultMind 49/50 Hit@1 vs
agent+grep 41/50) and fixed before the held-out run, which is what a held-out
set is for.

## Changes made for publication

Local absolute paths in READMEs and result files were rewritten to
repository-relative ones, and the closing housekeeping note of each set README
(about the private development repository) was removed. `sets/heldout/sha256sums.tsv`
was regenerated for the published files, because the README it covers changed. No question, label,
section note or result row changed. The `harness_git_sha` in `results/*/versions.json`
refers to the development repository where the freeze commit lives.
