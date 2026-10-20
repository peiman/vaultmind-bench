"""Section notes of a benchmark set.

A section note is an imported Markdown file that is not a parent index note.
The importer writes the parent index as `<stem>.md` beside a directory `<stem>/`
that holds the section files. This module never reads queries.yaml.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Note:
    id: str
    title: str
    body: str
    path: Path
    parent_doc_id: str
    parent_note_id: str


def _split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    return text[4:end], body


def _field(frontmatter: str, key: str) -> str:
    prefix = key + ":"
    for line in frontmatter.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def _read_note(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)
    note_id = _field(frontmatter, "id")
    title = _field(frontmatter, "title")
    if not note_id:
        raise SystemExit(f"imported note has no frontmatter id: {path}")
    return note_id, title, body


def _parent_doc_ids(set_dir: Path) -> dict[str, str]:
    """Map parent note id -> document id from sources.yaml, when present."""
    path = set_dir / "sources.yaml"
    if not path.is_file():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    documents = data.get("documents", data if isinstance(data, list) else [])
    out = {}
    for doc in documents or []:
        parent = doc.get("parent_id")
        doc_id = doc.get("id")
        if parent and doc_id:
            out[parent] = doc_id
    return out


def _is_parent_index(path: Path) -> bool:
    """True when `<stem>.md` sits beside the section directory `<stem>/`."""
    return path.suffix == ".md" and path.with_suffix("").is_dir()


def section_text(note: Note) -> str:
    """The text a system delivers for one section: title and body."""
    if note.title:
        return f"{note.title}\n\n{note.body}".strip()
    return note.body.strip()


def document_text(notes: list[Note]) -> str:
    """The parent document as the concatenation of its section texts, path order."""
    ordered = sorted(notes, key=lambda n: str(n.path))
    return "\n\n".join(section_text(n) for n in ordered)


def load(set_dir: str | Path) -> tuple[list[Note], list[Note]]:
    """Return (section notes, parent index notes) under vault/imported."""
    root = Path(set_dir)
    imported = root / "vault" / "imported"
    if not imported.is_dir():
        raise SystemExit(f"no imported notes at {imported}")
    doc_ids = _parent_doc_ids(root)
    parents: list[Note] = []
    parent_by_dir: dict[Path, Note] = {}
    sections: list[Note] = []
    files = sorted(p for p in imported.rglob("*.md") if p.is_file())
    for path in files:
        note_id, title, body = _read_note(path)
        if _is_parent_index(path):
            doc_id = doc_ids.get(note_id, note_id)
            note = Note(note_id, title, body, path, doc_id, note_id)
            parents.append(note)
            parent_by_dir[path.with_suffix("")] = note
        else:
            sections.append(Note(note_id, title, body, path, "", ""))
    resolved: list[Note] = []
    for note in sections:
        parent = parent_by_dir.get(note.path.parent)
        if parent is None:
            raise SystemExit(f"section note has no parent index beside it: {note.path}")
        resolved.append(
            Note(
                note.id,
                note.title,
                note.body,
                note.path,
                parent.parent_doc_id,
                parent.id,
            )
        )
    return resolved, parents


def sections(set_dir: str | Path) -> list[Note]:
    found, _parents = load(set_dir)
    return found
