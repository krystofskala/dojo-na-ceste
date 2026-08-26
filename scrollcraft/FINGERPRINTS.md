# Fingerprints

Every site you build with **scrollcraft** gets one row here, appended after it
ships. The registry exists so your next build can prove it is a different page
rather than a re-skin of one you already made.

This file is **yours**. It starts empty on purpose: the gate is about not
repeating *yourself*, so it has nothing to say until you have built something.

The rules and the gate live in the skill's
`references/uniqueness.md`. Short version:

**A new build must differ from EVERY row below on at least 4 of the 6
dimensions.** Four against each row individually, not four on average across the
table. If a planned build fails, change the plan. Never edit a row to make room
for it.

The six dimensions are: **grammar**, **nav treatment**, **hero device**,
**act-sequence shape**, **close pattern**, **signature move**.

Dimension 6 is free, because a signature move is unique by definition. So the
gate really asks for three more out of the remaining five, and a build that
changes only grammar and world will fail it.

---

## The registry

| Build | Grammar | Nav treatment | Hero device | Act-sequence shape | Close pattern | Signature move | World | Port |
|---|---|---|---|---|---|---|---|---|
| dojo-na-ceste | Chaptered editorial | Margin folio, chapter number + title, no fixed bar | Title page: type only on paper, no media above the fold | 7 units (title + 6 chapters), ~16.4vh, devices flow→reveal→pan→flow(horiz. scroller)→pan→flow→pin, zero scrub | Colophon/masthead: small type, real photo in a second column, CTA as a line of running text, resolves and holds | Coming into focus: a handful of recovered-lost activity cards sit blurred/faded inside a wide real-archive rail and sharpen only as they cross the viewport's horizontal centre, reading live `getBoundingClientRect()` position every frame | Photographic (Ch. I, II, colophon) + real archived fan art, all 4 pieces (Ch. III) + plain type on flat grounds (Ch. IV, V), real assets throughout, no generated ones | localhost:4517 (dev), build at scrollcraft/builds/dojo-na-ceste |

---

## What is taken

Add a bullet here whenever a build claims something a later build should avoid
reusing: a grammar, a nav treatment, a close pattern, a signature move, an
act-count-and-length band. The shared columns are what the next build inherits
as a constraint, so writing them down is the whole point.

- Chaptered editorial grammar, margin-folio nav, and a type-only title page (no media above the fold) are taken.
- Zero-`scrub` builds (photographic, no video) are taken as a valid route, not just a fallback.
- The "elements sharpen from blur/fade as they cross a fixed screen position, read from live layout each frame" family of signature move is taken.
- A wide real-archive `pan` rail as the peak chapter (not a vertical/pinned chronicle) is taken.
- The 6-unit / ~13.2vh act-sequence shape at flow→reveal→pin→pan→flow→pin is taken.

---

## Appending a row

After shipping, add one line to the table and one bullet to **What is taken** if
the build claimed something new. Fill every column. Say what the build shares
with existing rows.

Rows are append-only. A build that has been superseded stays in the table,
because the space it occupies is still occupied.

---

## Worked example

The skill's author kept a registry of twelve builds across eight page grammars.
If you want to see what a filled-in table looks like, and which shapes tend to
collide, read `EXAMPLES.md` in the scrollcraft repository. Treat it as
illustration only: those rows are somebody else's builds and they do **not**
constrain yours.
