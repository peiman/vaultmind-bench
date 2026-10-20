# Public benchmark held-out set — project knowledge for coding agents

**Date: 2026-10-16. This is a frozen held-out set. It is a judge, not a
tuning set.** Freeze every candidate retrieval and delivery strategy (and its
budgets and settings) before running it here. Do not choose, tune, or reject
strategies based on its results. Tune on the dev set
(`sets/devB/`) instead. If a result here leads to a
change, the changed strategy needs a new held-out set before anyone can claim
it generalises.

The set has 50 natural agent-style questions over six long public technical
documents that a coding agent would plausibly consult. Each question is
answered by exactly one imported section note. The procedure mirrors devB:
the same importer, a section note as the delivery unit, a verbatim keyphrase
per label, `first_block` labels, and a file-only validator. It adds one rule:
every keyphrase must occur in exactly one section note in the vault.

## Blindness statement

The questions, `expected` IDs, keyphrases and `first_block` labels were written
by reading the imported Markdown files directly. **The only VaultMind commands
that ever ran on this corpus were `vaultmind init` and `vaultmind import`.**
Every command ran with `VAULTMIND_APP_EMBED_ON_WRITE=false`. Each import
reported that the vault "has never been embedded", so no model computed
embeddings. These are the exact commands, all run on 2026-10-16 from the
repository root:

```sh
export VAULTMIND_APP_EMBED_ON_WRITE=false
vaultmind init sets/heldout/vault
vaultmind import https://www.rfc-editor.org/rfc/rfc6455.html --vault sets/heldout/vault --json   # rejected, see below
vaultmind import https://docs.python.org/3.13/library/subprocess.html --vault sets/heldout/vault --json
vaultmind import https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ --vault sets/heldout/vault --json
vaultmind import https://doc.rust-lang.org/cargo/reference/config.html --vault sets/heldout/vault --json
vaultmind import https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS --vault sets/heldout/vault --json
vaultmind import https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax --vault sets/heldout/vault --json
vaultmind import https://www.rfc-editor.org/rfc/rfc9113.html --vault sets/heldout/vault --json
```

No `vaultmind ask`, `search`, `eval`, `note`, `index`, `recall`, `context-pack`
or `mcp` command ran over this vault. No embedding, ranking, similarity
calculation, result-pool inspection or delivery scoring ran either. The
importer refreshes its own derived SQLite index after writing notes. That
index was never queried. It was deleted unread before the set was frozen,
because it still listed the rejected RFC 6455 notes. It is gitignored. No
other evaluation set's questions, notes or results were read. The only
earlier files opened were devB's procedural files (README, sources, queries
format, validator), used to copy the procedure and its exclusions. Labels
were checked only by literal string matching (`validate.py`).

## Sources and corpus

All pages were fetched by `vaultmind import` (which fetches one page and
converts it to Markdown) on **2026-10-16, Europe/Stockholm (UTC+02:00)**,
between 20:10 and 20:12 UTC. The committed imported notes *are* the snapshot.
`sources.yaml` records each page's SHA-256, URL, license, license URL, the
basis for redistribution, the attribution, the parent ID and the section
counts. Use the committed snapshot, not the live pages, which can change.

| Document | URL | License | Questions | Section notes |
|---|---|---|---:|---:|
| RFC 9113: HTTP/2 | https://www.rfc-editor.org/rfc/rfc9113.html | IETF Trust Legal Provisions (TLP 5.0 §3.c) | 8 | 68 |
| Python 3.13 `subprocess` reference | https://docs.python.org/3.13/library/subprocess.html | PSF License v2 (examples also 0BSD) | 9 | 24 |
| Kubernetes Deployments | https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ | CC BY 4.0 | 9 | 25 |
| The Cargo Book: Configuration | https://doc.rust-lang.org/cargo/reference/config.html | MIT OR Apache-2.0 (redistributed under MIT) | 8 | 19 |
| MDN: Cross-Origin Resource Sharing (CORS) | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS | CC BY-SA 2.5+ (code samples CC0) | 8 | 14 |
| GitHub Docs: Workflow syntax for GitHub Actions | https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax | CC BY 4.0 (code MIT) | 8 | 69 |

There are **219 section notes plus six parent index notes, 225 notes in
total**. Every document is longer than the importer's 32,768-character
splitting threshold, so each became a parent index note plus numbered section
notes. The smallest is MDN, whose section bodies total 34,419 characters.
Labels refer to actual imported section-note IDs. A hit on the parent, or on
a different section of the right document, does not count as the labelled
answer. Some section titles are importer artifacts and do not describe the
section's content. For example, Cargo's first section is titled "Keyboard
shortcuts" because the page chrome came first, but it also holds the
config-file hierarchy. A few Kubernetes sections are titled "Note:". These
titles are kept as imported, because a real agent would see the same ones.

**Excluded documents.** No document from an earlier set is used. The excluded
documents are devB (Redis Cluster spec, Kubernetes Pod Lifecycle, nginx HTTP
core module, RFC 9111, git-config, Python logging), the earlier held-out set
(SQLite WAL, PostgreSQL routine vacuuming, Python asyncio event loop, SQLite
query optimizer, the Go specification, the Dockerfile reference), and the old
dev set and its distractors (Effective Go, SQLite FTS5/FTS3, Python sqlite3,
Go memory model, Python dbm). `validate.py` enforces this list.

**Rejected document.** RFC 6455 (WebSocket) was imported first and then
rejected. Its rfc-editor.org page uses the legacy plain-text RFC rendering,
so the importer found no headings. It produced 28 "Part N" chunks whose text
sits inside code fences. Those sections can't be addressed by title, and
their prose can't be told apart from code. Its notes were deleted before any
question was written, and it has no questions. RFC 9113, which is published
in xml2rfc v3 HTML with real section headings, replaced it.

### Licenses and attribution

Every snapshot may be redistributed in a public repository under the terms
below. `sources.yaml` holds each document's full reasoning.

- **RFC 9113**: © 2022 IETF Trust and the persons identified as the document
  authors (M. Thomson, C. Benfield, Eds.). TLP §3.c(i)/(iii) allows copying
  and distributing unmodified RFC text with attribution, keeping the RFC's
  legends. The text is unmodified apart from HTML-to-Markdown conversion and
  splitting. The RFC's Copyright Notice is kept in section note
  `01-introduction`.
- **Python `subprocess` docs**: Copyright © 2001-2026 Python Software
  Foundation; All Rights Reserved. Licensed under the PSF License Version 2.
  The agreement is in `LICENSES/python-LICENSE.txt`.
- **Kubernetes Deployments**: © 2026 The Kubernetes Authors, CC BY 4.0
  (https://creativecommons.org/licenses/by/4.0/). Changed by converting to
  Markdown and splitting into section notes.
- **Cargo Book, Configuration**: © The Cargo Project Developers, dual
  MIT/Apache-2.0 (source in `rust-lang/cargo`, `doc/book/src/reference/config.md`).
  Redistributed under MIT; see `LICENSES/cargo-LICENSE-MIT.txt`.
- **MDN CORS guide**: "Cross-Origin Resource Sharing (CORS)" by Mozilla
  Contributors, CC BY-SA 2.5 or later. Changed by converting to Markdown and
  splitting into section notes. These snapshot files stay under CC BY-SA.
- **GitHub Docs workflow syntax**: © GitHub, Inc., CC BY 4.0 (github/docs
  `LICENSE`). Changed by converting to Markdown and splitting into section
  notes.

## Questions, labels and formats

The 50 questions are spread 8–9 per document. Each `expected` ID belongs to a
different section note. The questions are written the way a working agent
asks: usually a symptom or a task rather than a lookup. Many deliberately
avoid the section's vocabulary. For example, "a callback that runs in the
child just before the new program starts" targets `preexec_fn` without naming
it, and "how should an HTTP/2 server drain a connection during a deploy?"
targets RFC 9113's GOAWAY section without naming GOAWAY. Others reuse the
document's own terms, as agents also do.

**37 questions have `first_block: false` and 13 have `true`.** Each document
has two first-block questions, except Kubernetes, which has three.
`first_block` follows devB's definition. It says whether the keyphrase falls
in the note's *first prose block*: the first paragraph or prose list left after
excluding fenced code, headings, API signatures, standalone labels
(admonition titles, converter language tags such as `js`/`http`, short
definition terms ending in `:`, Cargo's `- Type/Default/Environment`
metadata lines), link-only anchors, image lines and importer footers. Inline
Markdown is preserved. Internal subheadings do not reset block numbering. In
numbered continuation parts, counting starts at that part's first prose block.

`queries.yaml` uses devB's flat YAML sequence of `name`/`text`/`expected`
records. `id` repeats `name`, `doc` keys into `sources.yaml`, and `keyphrase`
and `first_block` carry label metadata. `expected` is a one-element list
holding the answer note's frontmatter ID. `keyphrases.tsv` has two
tab-separated columns (question ID and keyphrase) and no header.
`evidence.tsv` records each keyphrase's note path, one-based prose-block
number, zero-based character offset into the note body (frontmatter
excluded), block length, body length and `first_block`. Together these make
the labels auditable without running retrieval.

Every keyphrase has 3–8 whitespace-separated words. Each one is a
case-sensitive literal substring of its labelled note's prose, with code and
metadata excluded. Each one occurs in no other section note in the vault.
Whether the labelled note fully answers its question was checked by reading
it, not inferred from the phrase match. No normalisation, approximate
matching, ranking or semantic model is used anywhere in verification.

## File-only validation

Run with Python 3 and PyYAML, from any directory:

```sh
python3 sets/heldout/validate.py
```

The validator checks:

- 50 unique IDs and question texts, and six documents, none of them on the
  exclusion list
- the blindness metadata: only `init`/`import` commands are listed, and no
  embedding ran
- a license, license URL and redistribution basis for every document
- 8–9 questions per document
- that every expected ID exists, is a section note (not a parent) of the
  right document, and is used by only one question
- keyphrase length, literal prose match and vault-wide uniqueness
- `first_block` labels against the computed block positions
- YAML/TSV agreement and the recorded evidence locations
- section counts and long-document sizes, the snapshot hashes, and every
  frozen file hash in `sha256sums.tsv`

It reads only files inside this directory. It never reads an index or any
other evaluation set, and it doesn't judge retrieval quality.

`.gitignore` excludes the derived SQLite index and the runtime fingerprint.
To evaluate, rebuild the index and embeddings from the committed notes
(`vaultmind index --full --embed --vault <this>/vault`) only *after* the
strategies under test are frozen. Keep run outputs outside this directory.

## Tool version

Installed `vaultmind` **v0.10.14**, commit
`cb53557ab5da60b182d42027e40d663b2a7f3518`, backend **ort+cpu**. `init`
created a fresh knowledge vault, and its two example notes were removed
before importing. URLs were imported one at a time and sequentially, with no
crawling.
