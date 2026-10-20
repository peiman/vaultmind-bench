#!/usr/bin/env python3
"""File-only checks for blind held-out labels.

Never reads an index, embeddings, or any other evaluation set. Adapted from
sets/devB/validate.py: the nginx-specific code-fence
rule is gone, generic standalone labels are masked, the BGE-M3 indexing record
is replaced by license and blindness metadata checks (no index or embedding
ran over this corpus), and keyphrases must be unique across the whole vault.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parent
FETCHED_DATE = "2026-10-16"

# Documents already used by earlier VaultMind long-document sets (held-out,
# devB, old dev set and its distractors). None may appear here.
EXCLUDED_URLS = {
    # earlier held-out long-document set
    "https://www.sqlite.org/wal.html",
    "https://www.postgresql.org/docs/18/routine-vacuuming.html",
    "https://docs.python.org/3.13/library/asyncio-eventloop.html",
    "https://www.sqlite.org/optoverview.html",
    "https://go.dev/ref/spec",
    "https://docs.docker.com/reference/dockerfile/",
    # old development set and distractors
    "https://go.dev/doc/effective_go",
    "https://www.sqlite.org/fts5.html",
    "https://docs.python.org/3.13/library/sqlite3.html",
    "https://www.sqlite.org/fts3.html",
    "https://go.dev/ref/mem",
    "https://docs.python.org/3.13/library/dbm.html",
    # devB (2026-10-12)
    "https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/",
    "https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/",
    "https://nginx.org/en/docs/http/ngx_http_core_module.html",
    "https://www.rfc-editor.org/rfc/rfc9111.html",
    "https://git-scm.com/docs/git-config/2.51.1",
    "https://docs.python.org/3.13/library/logging.html",
}

# Standalone labels that are not prose: admonition titles, code-language
# tags left by the HTML converter, separators.
LABELS = {
    "Note", "Note:", "Notes:", "Warning", "Warning:", "Caution", "Caution:",
    "Tip", "See also", "Examples:", "Example:", "Parameters:", "Format",
    "Description", "Default:", "* * *", "YAML", "yaml", "js", "http", "bash",
    "shell", "sh", "toml", "json", "text", "console", "python",
}


def read_note(path):
    raw = path.read_text()
    assert raw.startswith("---\n"), path
    _, frontmatter, body = raw.split("---", 2)
    return yaml.safe_load(frontmatter), body


def is_label(stripped):
    """A standalone label: listed, or a short heading-like line ending in ':'
    (definition terms such as `idle:` or `ACK (0x01):`, list intros such as
    `In this example:`), or a `- Type:/Default:/Environment:` metadata line."""
    if stripped in LABELS:
        return True
    if stripped.endswith(":") and len(stripped.split()) <= 4:
        return True
    return bool(re.match(r"^- (Type|Default|Environment): ", stripped))


def prose_blocks(body):
    """Preserve literal text and offsets while masking non-prose lines.

    The unit is the imported section note, including numbered continuation
    parts. Internal headings do not reset its first-block position.
    """
    masked = []
    fenced = False
    for line in body.splitlines(keepends=True):
        stripped = line.strip()
        fence = bool(re.match(r"^\s*(?:>\s*)?(```|~~~)", line))
        excluded = fenced or fence
        if fence:
            fenced = not fenced
        excluded |= bool(re.match(r"^\s*#{1,6}\s", line))
        excluded |= stripped.startswith(("Part of [[", "<!--", "!["))
        excluded |= is_label(stripped)
        excluded |= bool(re.match(r"^(?:\*class\*\s|\*exception\*\s|\S+\(.*\)\[¶\]|[\w.\\]+\[¶\])", stripped))
        excluded |= bool(re.fullmatch(r"(?:\[¶\]\([^\n]+\)|\[\]\([^\n]+\)(?:`[^`]+`|\w+)?|\[\[[^\n]+\]\])", stripped))
        masked.append(re.sub(r"[^\n]", " ", line) if excluded else line)
    text = "".join(masked)
    return [(m.start(), m.end(), m.group()) for m in
            re.finditer(r"\S[^\n]*(?:\n(?=[^\n]*\S)[^\n]*)*", text)]


def frozen_files():
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and p.name != "sha256sums.tsv"
                  and "__pycache__" not in p.parts
                  and not p.name.startswith("index.db")
                  and p.name != "fingerprint.txt")


def validate(check_manifest=True, check_derived=True):
    queries = yaml.safe_load((ROOT / "queries.yaml").read_text())
    sources = yaml.safe_load((ROOT / "sources.yaml").read_text())
    assert len(queries) == 50
    assert len(sources["documents"]) == 6
    assert len({q["id"] for q in queries}) == 50
    assert len({q["text"] for q in queries}) == 50
    docs = {d["id"]: d for d in sources["documents"]}
    assert len({d["url"] for d in docs.values()}) == 6
    assert not ({d["url"] for d in docs.values()} & EXCLUDED_URLS)
    blind = sources["blindness"]
    assert blind["vaultmind_commands"] and all(
        c.split()[1] in {"init", "import"} for c in blind["vaultmind_commands"])
    assert blind["embedding"] == "none"
    for doc in docs.values():
        assert doc["license"] and doc["license_url"].startswith("https://"), doc["id"]
        assert doc["redistribution"], doc["id"]
    notes = {}
    for path in sorted((ROOT / "vault/imported").rglob("*.md")):
        meta, body = read_note(path)
        assert meta.get("type") and meta.get("url"), path
        assert meta["id"] not in notes, meta["id"]
        notes[meta["id"]] = (path, meta, body)
    for doc in docs.values():
        members = [n for n in notes.values() if n[1]["url"] == doc["url"]]
        sections = [n for n in members if n[1]["id"] != doc["parent_id"]]
        assert len(sections) == doc["section_notes"] > 1
        assert len(members) == len(sections) + 1
        assert sum(len(n[2]) for n in sections) == doc["section_body_characters"] > 32768
        assert doc["fetched_date"] == FETCHED_DATE
        assert len(doc["snapshot_sha256"]) == len(members)
        for path, _, _ in members:
            rel = str(path.relative_to(ROOT))
            assert sha256(path.read_bytes()).hexdigest() == doc["snapshot_sha256"][rel]
    assert len(notes) == sum(d["section_notes"] + 1 for d in docs.values())
    evidence = []
    for q in queries:
        assert q["name"] == q["id"]
        assert isinstance(q["first_block"], bool)
        assert len(q["expected"]) == 1
        assert q["expected"][0] in notes, (q["id"], "expected note ID does not exist")
        path, meta, body = notes[q["expected"][0]]
        doc = docs[q["doc"]]
        assert meta["url"] == doc["url"]
        assert meta["id"] != doc["parent_id"]
        phrase = q["keyphrase"]
        assert 3 <= len(phrase.split()) <= 8, (q["id"], phrase)
        assert phrase in body, (q["id"], "not a literal body substring", phrase)
        holders = [nid for nid, (_, _, b) in notes.items() if phrase in b
                   and nid not in {d["parent_id"] for d in docs.values()}]
        assert holders == [meta["id"]], (q["id"], "keyphrase not unique", holders)
        blocks = prose_blocks(body)
        hits = [(i, start, text) for i, (start, _, text) in enumerate(blocks, 1)
                if phrase in text]
        assert hits, (q["id"], "not literal prose", phrase)
        ordinal, start, block = hits[0]
        assert q["first_block"] == (ordinal == 1), (q["id"], ordinal, phrase)
        evidence.append((q["id"], str(path.relative_to(ROOT)), ordinal,
                         start + block.index(phrase), len(block), len(body), q["first_block"]))
    assert len({q["expected"][0] for q in queries}) == 50, "two questions share a note"
    counts = Counter(q["doc"] for q in queries)
    assert all(8 <= n <= 9 for n in counts.values()) and len(counts) == 6
    assert all(counts[d["id"]] == d["questions"] for d in docs.values())
    split = Counter(q["first_block"] for q in queries)
    assert split[False] >= 30 and split[True] > 0
    if check_derived:
        tsv = (ROOT / "keyphrases.tsv").read_text().splitlines()
        assert tsv == [q["id"] + "\t" + q["keyphrase"] for q in queries]
        expected = ["id\tnote\tprose_block\tcharacter_offset\tblock_characters\tnote_body_characters\tfirst_block"]
        expected += ["\t".join(str(x).lower() if isinstance(x, bool) else str(x) for x in row)
                     for row in evidence]
        assert (ROOT / "evidence.tsv").read_text().splitlines() == expected
    if check_manifest:
        manifest = dict(line.split("\t", 1)[::-1] for line in
                        (ROOT / "sha256sums.tsv").read_text().splitlines())
        assert set(manifest) == {str(p.relative_to(ROOT)) for p in frozen_files()}
        for rel, digest in manifest.items():
            assert sha256((ROOT / rel).read_bytes()).hexdigest() == digest, rel
    print(f"Verified {len(queries)} questions: all {len(queries)} expected IDs exist; "
          f"all keyphrases are literal 3–8-word prose substrings of their labelled "
          f"note and occur in no other section note; first_block true={split[True]}, "
          f"false={split[False]}; {len(notes)} notes; counts={dict(counts)}")
    return evidence


if __name__ == "__main__":
    validate()
