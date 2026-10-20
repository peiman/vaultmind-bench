# Long-document dev set B — labelled blind

**This is a development set for choosing and tuning delivery strategies.**
Strategies, budgets, paragraph selection, and other candidate settings may be
tuned on this set after its freeze commit. The separate held-out long-document
set remains the judge: freeze candidates before evaluating there, and do not
use its results to tune them.

This corpus contains 50 natural agent-style questions over six long public
technical documents. Labels were written by reading the imported Markdown
files directly. No `vaultmind ask`, `search`, `eval`, or other retrieval,
ranking, similarity calculation, result-pool inspection, or delivery scoring
ran over this vault before the commit that added this directory. Importing and
embedding were the only VaultMind operations used on its corpus. The freeze
commit SHA is reported separately, rather than embedded recursively here.

The held-out directory was never opened except for its README, explicitly
permitted for the procedure and source exclusions. Its questions, notes,
index, and results were not read, queried, or reused. No old question fixtures
were read or reused either. Document exclusion was checked against the lists
provided in the request and the permitted procedural README.

## Sources and corpus

All retained pages were fetched on **2026-10-12 in Europe/Stockholm
(UTC+02:00)**, during 2026-10-11 UTC. `sources.yaml` records the URLs, local
fetch date, tool version, parent IDs, section counts, and SHA-256 of each
imported snapshot. Use these committed snapshots, rather than refreshing the
live documentation, when comparing strategies. RFC 9111 is a fixed standard;
Git and Python use versioned documentation. The other official documentation
pages can evolve, so the committed files are the stable evaluation corpus.

| Document | URL | Questions | Section notes |
|---|---|---:|---:|
| Redis Cluster specification | https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/ | 9 | 38 |
| Kubernetes Pod Lifecycle | https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ | 9 | 29 |
| Nginx HTTP core module reference | https://nginx.org/en/docs/http/ngx_http_core_module.html | 8 | 14 |
| RFC 9111: HTTP Caching | https://www.rfc-editor.org/rfc/rfc9111.html | 8 | 31 |
| Git 2.51.1 git-config reference | https://git-scm.com/docs/git-config/2.51.1 | 8 | 62 |
| Python 3.13 logging reference | https://docs.python.org/3.13/library/logging.html | 8 | 18 |

There are **192 section notes plus six parent index notes = 198 notes**.
Every retained document exceeds the importer's 32,768-character splitting
threshold. The importer merges small headings and divides oversized sections
into numbered continuation parts. Labels refer to actual imported section
note IDs. A parent hit or a different section of the right document is not
the labelled answer.

Excluded held-out documents are SQLite WAL, PostgreSQL routine vacuuming,
Python asyncio event loop, SQLite query optimizer, the Go specification, and
the Dockerfile reference. Excluded old development documents are Effective
Go, SQLite FTS5, and Python sqlite3; the old distractors named in the procedural
README (SQLite FTS3, Go memory model, Python dbm) are also absent.
Redis persistence and Nginx's main core reference were initially imported but
fell below the splitting threshold. They were removed before labelling and
embedding, and have no questions or retained notes.

## Later-paragraph bias and formats

**38 questions have `first_block: false`; 12 have `first_block: true`.**
Each document has two first-block questions; Redis and Kubernetes each have
seven later-block questions, and the other documents each have six.

The delivery unit is the labelled imported section note. Its *first prose
block* is the first paragraph or prose list remaining after excluding fenced
code, headings, API signatures, directive syntax/default/context metadata,
standalone labels, link-only anchors, image lines, and importer footers.
Inline Markdown is preserved. Technical version statements count as prose.
Internal subheadings do not reset the note's block numbering; for numbered
continuation parts, counting begins at that part's first retained prose block.
This measures whether delivery of the note's opening prose contains the
answer evidence. A false label does not imply the answer is beyond the
embedding model's token limit.

`evidence.tsv` records the exact note path, one-based prose-block number,
zero-based character offset into the Markdown body excluding frontmatter,
prose-block length, note-body length, and `first_block`. These locations make
the later-paragraph labels auditable without running retrieval. The keyphrase
is evidence for the answer; full answer sufficiency was checked by direct
reading, not inferred from a matching phrase alone.

`queries.yaml` uses the procedural README's flat YAML sequence of
`name` / `text` / `expected` records. `id` repeats `name`, `doc` keys into
`sources.yaml`, and `keyphrase` and `first_block` provide label metadata.
`expected` is a one-element list containing the answer note's frontmatter ID.
The evaluation loader can ignore the additional metadata.
`keyphrases.tsv` has exactly two tab-separated columns, question ID and
keyphrase, with no header.

All **50 keyphrases contain 3–8 whitespace-separated words**, and all pass a
case-sensitive literal substring check in their labelled note body and in
prose with code and metadata excluded. No normalization, approximate matching,
retrieval ranking, or semantic model is involved in verification.

## Build and file-only validation

Used installed `vaultmind`, **v0.10.9**, commit
`90fc6731ec8aadf5d1b1773b7a26e86b0f603978`, backend **ort+cpu**.
Read `vaultmind import --help` first, initialized a fresh knowledge vault,
and removed its two example notes. Imported each retained URL individually,
without crawling:

```sh
vaultmind init sets/devB/vault
vaultmind import <source-url> --vault sets/devB/vault --json
vaultmind index --full --embed --model bge-m3 --vault sets/devB/vault --json
```

Two imports briefly overlapped, which produced SQLite lock warnings in their
automatic indexing. Their section files were written successfully. The final
full rebuild indexed the retained corpus and computed BGE-M3 embeddings;
`indexing.json` records its completion. The rebuild also removes the discarded
short-document and scaffold entries from the derived index.

`.gitignore` excludes the rebuildable SQLite index, its transient files, and
the runtime fingerprint. The vault type registry and all source-note files
are committed. `sha256sums.tsv` freezes all retained input and documentation
files plus the completion record and validator; Git freezes the manifest.

Run the file-only validator with Python 3 and PyYAML, from any directory:

```sh
python3 sets/devB/validate.py
```

It checks the 50 unique IDs and texts, six source documents and exclusions,
8–9 questions per document, target-note membership, exact phrase lengths and
prose matches, YAML/TSV agreement, block-position labels, recorded evidence
locations, section counts and long-document sizes, source snapshot hashes,
successful BGE-M3 indexing, and all frozen file hashes. It reads only files
inside this directory, never an index or any other evaluation set. It does
not assess retrieval quality or automatically judge answer semantics.

## Use after freezing

Run delivery-strategy experiments only after the freeze commit. Compare
section retrieval and delivery of evidence separately, including per-document
and first-block/later-block breakdowns. Keep run outputs outside the frozen
inputs. Because this is a dev set, selecting strategies from its results is
allowed. Keep its input snapshot fixed to make those comparisons reproducible.
Use the untouched held-out set only to judge the subsequently frozen choice.
