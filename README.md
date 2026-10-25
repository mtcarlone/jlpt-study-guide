# JLPT Study Guide

An interactive N5 / N4 grammar quiz built from `_quiz_bank.md`, hosted on GitHub Pages.

**Live quiz:** https://mtcarlone.github.io/jlpt-study-guide/

## Quiz modes

- Sentence → grammar point
- Japanese → English
- English → Japanese
- Definition → grammar point
- Study notes: term → meaning
- Study notes: kanji → reading

Missed questions are re-asked at the end of each quiz until answered correctly, and are remembered in the browser for "Only questions I've missed".

Keys: `1`–`4` answer, `Space` (or tapping anywhere outside the buttons) shows/hides furigana, `Enter` goes to the next question.

## Updating the questions

Edit `_quiz_bank.md`, then regenerate the quiz data:

```sh
python3 scripts/build_quiz.py
```

This writes `docs/data.json`. Commit and push both files; GitHub Pages redeploys automatically.

## Running locally

```sh
python3 -m http.server -d docs
```

Then open http://localhost:8000. (Opening `docs/index.html` directly from disk won't work, because the browser blocks it from loading `data.json`.)

## GitHub Pages setup

Settings → Pages → Source: **Deploy from a branch**, Branch: `main`, Folder: `/docs`.
