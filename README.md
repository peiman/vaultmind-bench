# Project knowledge for coding agents

A small, reproducible benchmark for one question: **when a coding agent needs an
answer that lives in a project's long technical docs, which retrieval puts the
right section in front of it, and at what token cost?**

Most agent-memory benchmarks measure chat recall. This one measures lookups in
documentation: 50 questions over six long public docs, each answered by exactly
one section, labelled by reading the files before any system ran.

## Result (held-out set, single run)

| system | Hit@1 | Hit@3 | tokens per answer | seconds per answer |
|---|---:|---:|---:|---:|
| [VaultMind](https://github.com/peiman/vaultmind) `ask` alone | 32/50 | 45/50 | 2,611 | 2.5 |
| BM25 (SQLite FTS5) | 28/50 | 38/50 | 2,582 | 0.0 |
| ripgrep, keyword ranking | 20/50 | 32/50 | 3,284 | 0.1 |
| an agent driving grep (Claude Haiku 5.5) | 42/50 | 44/50 | 8,086 | 7.0 |
| the same agent with VaultMind as a tool | 46/50 | 49/50 | 5,902 | 8.8 |
| paste the whole document | — | — | 25,585 | — |

A hit means the one labelled section is at rank ≤ k. Tokens are counted with
tiktoken `cl100k_base` (the agents' from their reported usage). Details and the
dev-set numbers: [RESULTS.md](RESULTS.md).

**What it says.** An agent driving grep is a strong baseline: it beats every
non-agent system on first-pick accuracy, at about three times the tokens.
VaultMind alone ranks well above keyword search (Hit@3 45 vs 32 for ripgrep and
38 for BM25) with no model call per lookup. Given VaultMind as a tool, the agent
found 5 more answers in 50 and read 27% fewer tokens.

**What it does not say.** We pre-registered three claims before the held-out run
(see [METHOD.md](METHOD.md)). None held: VaultMind alone does not beat the agent
by 10 points, the agent with VaultMind does not use ≤ 60% of the tokens, and its
first-pick gain was 4 questions, one short of the 5 we required.

The benchmark was built by VaultMind's author. That is why the method, the
pre-registered claims, every system's raw output and the scorer are all here:
check the numbers, not the author.

## What's here

| path | contents |
|---|---|
| `sets/heldout/` | the judge: 50 questions, labels, sources, licenses, and the imported section notes (225 notes) |
| `sets/devB/` | the development set: 50 questions, labels, sources, and five of its six documents (Redis withheld, see below) |
| `harness/` | one runner per system, one scorer for all, `run_all.sh` |
| `results/` | raw per-question output of every system on every run, plus scores |
| `METHOD.md` | question, systems, metric, the freeze, and the pre-registered claims |

## Reproduce

Requirements: Python 3.11+, `ripgrep`, the VaultMind ORT release binary on PATH
(`vaultmind --version` → v0.10.15 for these numbers), and for the agent systems
the Claude Code CLI. `pip install tiktoken` for the same token counts.

```sh
bash harness/run_all.sh sets/heldout results/my-run
```

Agent runs are not deterministic; expect their numbers to move by a few
questions between runs (see the two dev-set runs in RESULTS.md).

## Limits

- **One author wrote and labelled the questions**, by reading the docs. Questions
  written that way can share words with the answer, which helps keyword search.
- **Single held-out run per system.** Agent baselines vary run to run.
- **50 questions** per set. One question is 2 points.
- **QMD** was planned as a baseline but did not run here; see `results/devB/qmd.skip`.
- **Dev B's Redis Cluster spec is withheld**: Redis documentation is CC BY-NC-SA 4.0,
  and we have not established which license covers this snapshot. Its nine questions,
  URL and snapshot hashes are included; a re-run here scores them as misses unless
  you import the page yourself. The other five dev B documents are included
  (`sets/devB/LICENSES/LICENSES.md`).

## Licenses

Harness code: MIT ([LICENSE](LICENSE)). The documents keep their own licenses,
recorded with attribution per document: held-out in `sets/heldout/sources.yaml`
(IETF TLP, PSF License, CC BY 4.0, MIT, CC BY-SA), dev B in
`sets/devB/LICENSES/LICENSES.md` (PSF License, CC BY 4.0, BSD 2-Clause, IETF TLP, GPL-2.0). Changes to them: HTML converted
to Markdown and split into section notes by `vaultmind import`.
