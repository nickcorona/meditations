# Meditations

Two files:

- `book.md`: the whole of Marcus Aurelius's Meditations, one entry per `## book.section` heading. Cue Home reads through it in order, one passage at a time, as many as I want. Don't edit the text. It starts as George Long's 1862 translation (public domain). When I upload my own copy of the Gregory Hays translation as `hays.txt` (the archive.org full-text file), the `Build book.md from hays.txt` workflow runs `tools/hays_to_book.py` and replaces `book.md` with it.
- `skip.md`: passages of `book.md` that Home leaves out, so the reader shows only principles: all of Book 1 (his thanks to people) and bare quotations, name lists and fragments. Add or remove lines to change what shows.
- `meditations.md`: my own short list of ideas, each tied to the situation it's for. Not shown on Home right now; kept for reference. The format below is strict.

## Format (do not deviate)

```
## <short id, kebab-case>
for: <the internal state that triggers it>
idea: <the idea in my words, one or two lines>
why: <one line on why I believe it>   (optional)
stage: read | recall
```

One blank line between entries. No other fields, no extra prose inside entries.

## Rules

- When I bring a passage or idea, push me to write the line myself, then help tighten it. Don't write it for me.
- Each entry is one idea, plus the trigger it's for. Plain language, no em dashes.
- Write `for:` as an internal state ("replaying what someone said"), not an external event ("someone criticized me").
- For something I'm avoiding, `idea:` is the small action to take, not a reframe.
- No cap on the list. Before adding one, check it isn't already covered by an existing entry; if it is, merge them instead.
- The file is ranked by usefulness, most useful first. Put a new entry where it ranks, not at the end; Cue introduces new entries in this order.
- Cue Home runs the list as spaced repetition: a new entry is shown in full once, then comes back as a recall test (trigger only; I recall the idea, tap to check, mark missed or got it) on growing intervals (1, 3, 8, 20, 50 days...). A miss brings it back the next day. The schedule lives in Cue, not in this file.
- `stage: recall` here means I already know it: Cue skips the first full showing and goes straight to testing. Leave new entries as `stage: read`.
- Rewrite lines in place when they stop landing or I catch myself reciting them on autopilot. Git history keeps the old wording, so no separate archive file.
- Commit and push after every change with a short message naming the entry (e.g. `add: replaying-criticism`, `reword: morning-dread`, `recall: other-peoples-opinions`).
