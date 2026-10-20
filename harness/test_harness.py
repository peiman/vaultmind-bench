"""Parsing and ranking tests for the public-benchmark harness.

Run from anywhere: python3 test_harness.py
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import corpus
import questions
import run_agent_rg
import run_bm25
import run_qmd
import run_rg
import run_vm
import run_whole
import score
import tokens

ROOT = Path(__file__).resolve().parents[3]
DEVB = ROOT / "experiments" / "2026-10-12-devB-longdoc"


class Note:
    def __init__(self, note_id, title, body, path="p"):
        self.id = note_id
        self.title = title
        self.body = body
        self.path = Path(path)


def test_tokens_method_and_count():
    assert tokens.METHOD in ("tiktoken-cl100k_base", "ceil(chars/4)")
    assert tokens.count("") == 0
    assert tokens.count("hello") >= 1
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "out.jsonl"
        tokens.write_jsonl(path, [{"name": "q", "ranked": [], "delivered_tokens": 1, "seconds": 0}])
        row = json.loads(path.read_text().strip())
        assert row["token_method"] == tokens.METHOD


def test_corpus_parent_is_not_a_section():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        imported = root / "vault" / "imported" / "web" / "example.com"
        section_dir = imported / "doc"
        section_dir.mkdir(parents=True)
        parent = imported / "doc.md"
        parent.write_text(
            "---\nid: parent-doc\ntitle: Parent\n---\nParent: 1 section.\n",
            encoding="utf-8",
        )
        (section_dir / "01-intro.md").write_text(
            "---\nid: parent-doc-01-intro\ntitle: Intro\n---\nHello section.\n",
            encoding="utf-8",
        )
        (root / "sources.yaml").write_text(
            "documents:\n  - id: example\n    parent_id: parent-doc\n",
            encoding="utf-8",
        )
        found, parents = corpus.load(root)
        assert [n.id for n in parents] == ["parent-doc"]
        assert [n.id for n in found] == ["parent-doc-01-intro"]
        assert found[0].parent_doc_id == "example"
        assert found[0].parent_note_id == "parent-doc"
        assert "Hello section." in found[0].body
        assert "id:" not in found[0].body


def test_devb_section_count():
    found, parents = corpus.load(DEVB)
    assert len(parents) == 6
    assert len(found) == 192
    parent_ids = {n.id for n in parents}
    assert parent_ids.isdisjoint({n.id for n in found})
    assert {n.parent_doc_id for n in found} == {
        "redis",
        "kubernetes",
        "nginx",
        "http_caching",
        "git_config",
        "python_logging",
    }


def test_prompts_hide_labels():
    labelled = questions.load(DEVB)
    assert len(labelled) == 50
    for question in labelled:
        assert question["expected"]
        assert "keyphrase" not in question
    for prompt in questions.prompts(DEVB):
        assert set(prompt) == {"name", "text", "doc"}


def test_bm25_ranks_the_matching_section_first():
    notes = [
        Note("hash", "Hash tags", "hash tags keep keys in one slot"),
        Note("nginx", "Nginx", "the worker process listens"),
    ]
    ranked = run_bm25.rank(notes, "What are hash tags meant to ensure?")
    assert ranked[0] == "hash"
    assert "nginx" not in ranked


def test_bm25_query_quotes_words():
    assert run_bm25.fts_query("hash tags?") == '"hash" OR "tags"'
    assert run_bm25.fts_query("...") == ""


def test_rg_content_words_and_rank():
    words = run_rg.content_words("How does the hash tag work in the cluster?")
    assert "how" not in words and "does" not in words and "the" not in words
    assert "in" not in words
    assert words == ["hash", "tag", "work", "cluster"]
    counts = {
        "c": {"hash": 1, "tag": 1},
        "a": {"hash": 1, "tag": 1},
        "b": {"hash": 5, "tag": 0},
        "z": {"hash": 0, "tag": 0},
    }
    paths = {"a": "/z/a.md", "c": "/a/c.md", "b": "/m/b.md", "z": "/a/z.md"}
    assert run_rg.rank_counts(counts, paths) == ["c", "a", "b"]


def test_rg_counts_lines():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        first = root / "one.md"
        second = root / "two.md"
        first.write_text("Hash tags\nhash again\n", encoding="utf-8")
        second.write_text("nothing here\n", encoding="utf-8")
        counts = run_rg.rg_counts("hash", [first, second])
        assert counts[str(first)] == 2
        assert str(second) not in counts


def test_agent_parses_fenced_array():
    text = 'Sure.\n```json\n["alpha.md", "./beta.md", "missing.md", "alpha.md"]\n```'
    valid = {"alpha", "beta"}
    assert run_agent_rg.ranked_ids(text, valid) == ["alpha", "beta"]
    assert run_agent_rg.ranked_ids("no array here", valid) == []
    payload = {
        "usage": {
            "input_tokens": 41,
            "cache_creation_input_tokens": 100,
            "cache_read_input_tokens": 500,
            "output_tokens": 12,
        },
        "modelUsage": {"claude-haiku-4-5-20251001": {}},
    }
    assert run_agent_rg.delivered_tokens(payload) == 153
    assert run_agent_rg.usage_counts(payload)["cache_read_input_tokens"] == 500
    assert run_agent_rg.model_id(payload) == "claude-haiku-4-5-20251001"


def test_agent_vm_differs_from_agent_rg_only_by_vaultmind():
    import run_agent_vm

    assert run_agent_vm.PROMPT.startswith(run_agent_rg.PROMPT)
    assert "vaultmind ask" in run_agent_vm.PROMPT
    assert run_agent_vm.TOOLS == run_agent_rg.TOOLS + ",Bash"
    assert run_agent_vm.ALLOWED == run_agent_rg.TOOLS + ",Bash(vaultmind ask:*)"
    cmd = run_agent_rg.agent_command("q", run_agent_vm.TOOLS, run_agent_vm.ALLOWED)
    assert cmd[cmd.index("--model") + 1] == run_agent_rg.MODEL == "claude-haiku-5-5"
    assert "--restricted" in cmd


def test_vm_keeps_parent_position_and_counts_delivered_text():
    payload = {
        "status": "ok",
        "result": {
            "top_hits": [
                {"id": "parent-doc"},
                {"id": "parent-doc-01-intro"},
            ],
            "context": {
                "target": {"frontmatter": {"title": "Parent"}, "body": "index only"},
                "context": [
                    {"frontmatter": {"title": "Intro"}, "body": "the answer"},
                ],
            },
        },
    }
    ranked, text = run_vm.parse_ask(payload)
    assert ranked == ["parent-doc", "parent-doc-01-intro"]
    assert "index only" in text and "the answer" in text
    assert run_vm.parse_ask({"status": "ok", "result": {"top_hits": [], "context": None}}) == ([], "")


def test_whole_fit_boundary():
    assert run_whole.fits_200k(200_000) is True
    assert run_whole.fits_200k(200_001) is False


def test_score_parent_occupies_a_rank():
    labelled = [
        {"name": "q1", "expected": ["section"]},
        {"name": "q2", "expected": ["missing"]},
    ]
    rows = [
        {"name": "q1", "ranked": ["parent", "other", "section"], "delivered_tokens": 10, "seconds": 1.0},
        {"name": "q2", "ranked": ["parent"], "delivered_tokens": 4, "seconds": 3.0},
    ]
    result = score.score_rows(labelled, rows)
    assert result["hit_at_1"]["hits"] == 0
    assert result["hit_at_3"]["hits"] == 1
    assert result["misses"] == [
        {"name": "q2", "rank": None, "expected": ["missing"]},
    ]
    assert score.label_rank(["parent", "section"], ["section"]) == 2


def test_qmd_parser():
    payload = {"results": [{"file": "alpha.md", "score": 1}, {"path": "beta.md"}, {"file": "nope.md"}]}
    assert run_qmd.ranked_from_payload(payload, {"alpha", "beta"}) == ["alpha", "beta"]


def main():
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    failed = 0
    for test in tests:
        try:
            test()
        except Exception as exc:
            failed += 1
            print(f"FAIL {test.__name__}: {exc}")
        else:
            print(f"ok   {test.__name__}")
    if failed:
        raise SystemExit(f"{failed} failed")
    print(f"{len(tests)} passed")


if __name__ == "__main__":
    main()
