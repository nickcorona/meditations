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
- The file is ranked by usefulness, most useful first. Put a new entry where it ranks, not at the end; Cue introduces new entries in this order.
- Cue Home runs the list as spaced repetition: a new entry is shown in full once, then comes back as a recall test (trigger only; I recall the idea, tap to check, mark missed or got it) on growing intervals (1, 3, 8, 20, 50 days...). A miss brings it back the next day. The schedule lives in Cue, not in this file.
- `stage: recall` here means I already know it: Cue skips the first full showing and goes straight to testing. Leave new entries as `stage: read`.
- Rewrite lines in place when they stop landing or I catch myself reciting them on autopilot. Git history keeps the old wording, so no separate archive file.
- Commit and push after every change with a short message naming the entry (e.g. `add: replaying-criticism`, `reword: morning-dread`, `recall: other-peoples-opinions`).
