#!/usr/bin/env python3
"""Convert _quiz_bank.md into docs/data.json for the GitHub Pages quiz.

Usage: python3 scripts/build_quiz.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_quiz_bank.md"
OUT = ROOT / "docs" / "data.json"

ALLOWED_TAG = re.compile(r"&lt;(/?)(ruby|rt|br)&gt;")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def safe_html(text):
    """Escape everything, then re-allow only <ruby>, <rt> and <br>."""
    return ALLOWED_TAG.sub(r"<\1\2>", html.escape(text, quote=False))


def main():
    concepts, sentences, notes = {}, [], []
    section = "sentences"
    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Study notes"):
            section = "notes"
            continue
        if not line.startswith("| ") or line.startswith("| ID") or line.startswith("| ---"):
            continue
        c = cells(line)
        if section == "sentences":
            sid, level, concept, definition, ja, ja_plain, en = c
            key = sid.rsplit("-", 1)[0]  # e.g. N5-01
            concepts.setdefault(key, {"id": key, "level": level, "name": concept, "def": definition})
            sentences.append({"id": sid, "c": key, "ja": safe_html(ja), "plain": safe_html(ja_plain), "en": safe_html(en)})
        else:
            nid, ntype, level, term, reading, meaning, ex, ex_en = c
            notes.append({"id": nid, "type": ntype, "level": level, "term": term,
                          "reading": reading, "meaning": meaning, "ex": ex, "exEn": ex_en})

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"concepts": list(concepts.values()), "sentences": sentences, "notes": notes},
                              ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{len(concepts)} concepts, {len(sentences)} sentences, {len(notes)} notes -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
