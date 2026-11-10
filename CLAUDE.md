# Meditations

My personal version of Marcus Aurelius's Meditations: a short list of ideas in my own words, each tied to the situation it's for. A widget on the Cue Home screen parses `meditations.md`, so the format is strict.

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
- The file is ranked by usefulness, most useful first; Cue Home cycles through it in that order. Put a new entry where it ranks, not at the end.
- New entries start as `stage: read`. Cue moves one to recall on its own once I've read it on 5 different days. Flip it to `recall` here sooner if I say I can produce it, even shakily.
- Rewrite lines in place when they stop landing or I catch myself reciting them on autopilot. Git history keeps the old wording, so no separate archive file.
- Commit and push after every change with a short message naming the entry (e.g. `add: replaying-criticism`, `reword: morning-dread`, `recall: other-peoples-opinions`).
