# Results

## Held-out set (the result)

Single run, 2026-10-20, from the frozen harness.

| system | Hit@1 | Hit@3 | tokens per answer (mean) | seconds per answer |
|---|---:|---:|---:|---:|
| `vm` VaultMind `ask` alone | 32/50 | 45/50 | 2,611 | 2.5 |
| `bm25` | 28/50 | 38/50 | 2,582 | 0.0 |
| `rg` | 20/50 | 32/50 | 3,284 | 0.1 |
| `agent-rg` agent driving grep | 42/50 | 44/50 | 8,086 | 7.0 |
| `agent-vm` the same agent + VaultMind | 46/50 | 49/50 | 5,902 | 8.8 |
| `whole` paste the whole document | — | — | 25,585 | — |

Every held-out document fits a 200k-token context. Per-question misses for every
system: `results/heldout/scores.md`. Raw rows: `results/heldout/*.jsonl`.

## Dev B (development; used to build the harness)

Second run, both agents on Haiku 5.5:

| system | Hit@1 | Hit@3 | tokens | seconds |
|---|---:|---:|---:|---:|
| `vm` | 38/50 | 48/50 | 2,911 | 1.4 |
| `bm25` | 36/50 | 44/50 | 2,719 | 0.0 |
| `rg` | 30/50 | 45/50 | 3,201 | 0.1 |
| `agent-rg` | 41/50 | 48/50 | 6,774 | 6.5 |
| `agent-vm` | 49/50 | 49/50 | 6,410 | 6.8 |

First run (`results/devB-run1-haiku45/`), agent on Haiku 4.5, before `agent-vm`
existed: `agent-rg` 48/50 Hit@1, 49/50 Hit@3, 8,782 tokens. The same agent setup
scored 41/48 on the second run with the newer model; treat single agent numbers as
noisy by a few questions.

## Versions

VaultMind v0.10.15 (`a9cc401`, ORT, BGE-M3), ripgrep 15.2.0, Claude Code CLI
2.1.304 with `claude-haiku-5-5`, Python 3.14.8, tiktoken `cl100k_base`.
