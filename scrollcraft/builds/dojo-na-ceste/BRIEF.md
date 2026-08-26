# BRIEF — Dójó Na Cestě, scroll build

Self-authored from the existing project, at the user's explicit request
("fill the interview based on what we did in this project"). Not a fallback
for an unreachable human — the human is present and asked for this route
directly. Drawn from: index.html and the other page copy, data/site-content.json,
historie.html + design/old-sites-style-guide.md, css/style.css tokens, and the
real photos already in images/.

## Steer from the human, added after the initial draft

"I'd like it to be modern and interactive but also hit the open, non-commercial,
family feel. Minimal Japanese aesthetic." This sharpens rather than replaces the
self-authored answers below: minimal-Japanese pulls the palette toward more
negative space (ma) and restraint than a generic "premium-minimal" brand site
would use; modern/interactive raises the bar on the device variety and the
signature move rather than letting either be decorative; open/non-commercial/
family softens "quiet pride" toward "come as you are" — the pay-what-you-want
philosophy and the four-ages course row should read as genuine welcome, not
just as trust signals. Folded into the answers and the curve below.

## The eight answers

1. **Vibe, 3–5 words:** quiet, warm, unhurried, honest, grounded — and, per the
   steer above, openly *modern*: real interaction, not a static page with
   scroll-fade decoration, but never loud or salesy about it.
   References (not sites): a well-worn wooden dojo floor at dusk — plain
   material aging well, not polished. A hand-bound ledger that's never had a
   page torn out — the idea, literalized by this project's own `historie.html`,
   of an accumulating record nothing erases. The indigo-night mood of the
   original 2006 hand-coded site's torii banner (images/historie/era1-2007.jpg)
   — real and worth keeping, but rebuilt with actual contrast instead of the
   low-contrast slate-on-indigo that made it hard to read. Minimal Japanese
   aesthetic as the governing register: generous ma (negative space), few
   colours held strictly, one accent used sparingly, nothing decorative that
   isn't also structural.

2. **Scroll journey, in the project's own words:**
   1. Arrival — the mark, "nenásilná cesta" (a non-violent path), the blurred
      photo of a real throw (images/hero-home.jpg) — you're looking at a
      practice, not a gym ad.
   2. What aikido actually is — ai (harmony) + ki (energy) + dó (way);
      explicitly not competitive, not about winning.
   3. Who's been here — one sensei lineage (Michal "Lachim" Šíp → Radek
      Růžička → Miroslav Skala), a converted print-shop hall from 2004, and a
      real chronicle of what actually happened: posts that are still true
      today standing next to the activities that quietly disappeared from the
      site (revised after the human's feedback, see below).
   4. Pick your door in — Píďata 4–8, kids 8–14, adults, yoga. Four real
      photos, four real ages.
   5. The membership philosophy stated plainly — pay what you decide it's
      worth, from 0 Kč.
   6. Come train — first session, phone, address, one clear action.

3. **Energy curve:** calm at the open (arrival). Warm and intimate through
   philosophy and lineage — never loud. A quiet lift at the twenty-years/three-
   eras/nothing-erased beat — not louder, *fuller*, more scroll room, more
   weight. Levels back to plain and direct for courses, price, contact. The
   page never spikes into hype; the closest thing to "loud" here is warmth.

4. **Feeling, stage by stage, and the one moment:**
   - Arrival: "this is a place, not a business."
   - Philosophy: a small release — "oh, it's not about winning."
   - Lineage/history: **the peak.** "Twenty years, three different websites,
     and they never deleted a single line." Quiet pride, continuity, the
     specific kind of trust that comes from an institution that keeps its own
     record honestly (this project's historie.html even flags where the
     record contradicts today's official story, rather than smoothing it
     over — that honesty belongs in the peak, not just in a footnote).
   - Courses: clarity and welcome — "I know where I fit, and it looks like
     kids and adults are both genuinely home here" (family feel, not a
     segmented sales grid).
   - Price: trust and openness — "they mean it, it's not a gimmick, and they
     mean it for people who have nothing to give too."
   - Close: warm, low-friction invitation — "come as you are," not "convert
     now."

5. **Signature move (seed):** literalize "an accumulating record that nothing
   erases." As the visitor scrolls through the lineage/history beat, earlier
   material doesn't get replaced or swiped away — it settles underneath the
   current layer, like sediment, and stays visible at the edge as the next
   layer arrives on top. Three real artifacts already exist to drive it: the
   2007 site, the 2017 site, today's site (images/historie/era1-2007.jpg,
   era2-2017.jpg, era3-2026.jpg) — the visitor is scrolling through actual
   accumulated time, not a styled slideshow standing in for the idea.

6. **Aesthetic range:** premium-minimal, pulled toward minimal-Japanese per
   the human's steer — more negative space than a generic "premium-minimal"
   brand site would default to, restraint as the actual aesthetic rather than
   a placeholder for "not done yet." Editorial, quiet confidence — brutalist
   and maximalist are both wrong for a place whose philosophy is "nenásilná
   cesta," and "family/non-commercial" rules out anything that reads as a
   sales funnel (no urgency copy, no countdown framing, no stat-wall of
   invented numbers). The project's own css/style.css already made most of
   this call: warm paper (#f7f4ec), navy (#182338 / #101828), one muted
   terracotta-red accent (#a63d2c), Shippori Mincho serif heads + Inter body.
   Theme the build from these tokens rather than inventing new ones — it's the
   one considered palette this club has had in twenty years. Push the spacing
   and restraint further than the current static site does; it's the axis the
   steer is asking to move.

7. **One world or distinct scenes:** distinct scenes/chapters. The dojo's own
   truth is continuity of identity *through* visibly different eras, not one
   unbroken place — worldflight would fight the actual content. Chaptered/
   editorial grammar fits what's being said.

8. **What already exists (use this, don't generate):**
   - `images/hero-home.jpg` — real motion-blurred throw, strong hero-grade.
   - `images/o-nas-main.png` — sensei + kids, staffs, outdoor camp, a dog.
   - `images/{pidata,aikido-deti,aikido-dospeli,joga}-hero.jpg` — one photo
     per course.
   - `images/gallery/*` — training, 2025 summer camp, city camp, 10-year
     anniversary.
   - `images/historie/era1-2007.jpg`, `era2-2017.jpg`, `era3-2026.jpg` — real
     Wayback Machine captures (raw, with browser chrome; crop to the site
     banner/body when used so they read as artifacts, not screenshots).
   - `images/logo.gif` — the torii + 人 + 合気道 mark, the one piece of brand
     identity that survived all three eras.
   - `data/site-content.json`, `content/aktuality.md`, `data/aktuality.json`
     — the existing Czech copy, verbatim source for all page text.
   - No footage, so no video-scrub devices, and no ffmpeg on this machine
     either — the build stays photographic, not filmic. No KIE_AI_API_KEY set,
     so no generation budget; if a genuine asset gap turns up (nothing else
     covers a beat) say so rather than generating around the limits.

## Feeling curve

| Act | Emotion | What causes it |
|---|---|---|
| Arrival | Quiet, grounded | Blurred real throw, mark, "nenásilná cesta" stated plainly, no scroll cue |
| Philosophy | Small release | ai/ki/dó broken down; explicit "not competitive" |
| Kronika (**peak**) | Quiet pride, honesty | Real chronicle: five posts still true today next to four activities that quietly vanished, marked, not cut; a live tally counting both as they arrive |
| Courses | Clarity | Four ages, four real photos, one line each |
| Price | Trust | Pay-what-you-decide stated without hedging, from 0 Kč |
| Close | Warm invitation | One action, phone, address, resolves and holds |

## The peak

"Five things we still do, four we quietly stopped, and the site says so."
Lives in **Kronika**. It gets the tally signature move, the most scroll room,
and the quiet-before-it is the philosophy act settling rather than building
tension.

## Tell-someone sentence

It's the site where the history section counts, live, as you scroll: what
the dojo still does today, and what it quietly stopped doing, side by side,
neither one hidden.

## Revision, after the human saw the first build

Two changes, both direct feedback:

1. **Drop the "three websites" framing entirely.** The human didn't want the
   meta-narrative about the site's own redesign history. What they wanted
   instead: the real Wix-era posts (`data/aktuality.json`), plus the
   activities `historie.html` found had quietly vanished from the site (Ha
   Tha Jóga, Prožitkové zpívání, Meditace/Óm/pránajáma, Tchaj-ři čchüan).
   Chapter II is rebuilt around that: a chronicle of nine real dated entries,
   five still-standing posts and four recovered-but-lost activities, pulled
   verbatim from the project's own data rather than from the Wayback Machine
   screenshots. The signature move changed with it, see below.
2. **The 20% discount reads oddly next to "attendance is free."** True: a
   discount off a voluntary, pay-what-you-decide contribution is a strange
   thing to headline next to "0 Kč, genuinely." Cut it from Chapter IV's
   figures entirely rather than reframe it; the two real numbers that remain
   (0 Kč floor, 800 Kč recommended) don't have that tension.

## Second revision: the comic

The human, separately, asked to keep the Wix-era site's comic-style
illustrations, hand-drawn for the dojo by a friend. None of that was in the
project's own recovered content (`content/pages`, `data/aktuality.json`
mention origami and camp activities but not the artwork itself), so this
required going back to the actual Wayback Machine archive rather than
reusing anything already pulled into this repo. Queried the CDX index for
every URL ever archived under `aikidoricany.cz` (672 distinct URLs) and found
exactly one match: `img/KomiksOrigami.jpg`, a hand-inked black-and-yellow
comic page (1168×1653, archived 2013–2016) of a child folding origami who
dodges an armored samurai and, at the end, hands him the folded paper instead
of fighting. That is not incidental to this brief: it is the aikido
philosophy in Chapter I (harmony over confrontation, "necvičíme na výkon")
acted out panel by panel, drawn for this specific dojo by name. Saved to
`images/komiks-origami.jpg` in the main project (not just the build) since
it's a real recovered asset worth keeping regardless of this scroll page's
fate, and into the build's own `assets/`.

No artist name surfaced in the archive or in the project's own text, so the
caption credits it as "od kamaráda dójó" (from a friend of the dojo) rather
than inventing or guessing a name. Searched the full CDX list for anything
else in the same family (other comic pages, a dedicated "komiks" page in the
old nav) and found nothing more; if the human knows of other pieces (a
physical original, a different filename, a second page), point me at them
and they can go in the same slot.

Placed as a new **Chapter II, "Kresba"** (the drawing), between Cesta and
Kronika: it's a genuine quiet beat, exactly what the peak act needs
immediately before it, and it reinforces the "family, made by and for this
specific community" feel from the human's earlier steer better than anything
generated could. Chapters III–V (formerly II–IV) renumbered accordingly.

## Third revision: voice feedback on the built page

Six concrete points, taken in order:

1. **Chapter I: the photo didn't read as centred against the text.** True
   cause: `align-items:center` on the grid centres the image against the
   text column's full geometric height, eyebrow label included, but the
   eyebrow is small and the heading is what the eye anchors to, so the image
   looked like it started too high. Fixed with a top margin on the figure so
   it lines up with the heading instead of the label above it.
2. **Chapter II, the comic: the human has three more, not one.** A yellow
   comic with a boy (already in, the origami/samurai page), plus a red one,
   a blue one with a samurai, and a grey one with an old man, each with its
   own profile picture, meant to be used throughout the site rather than
   siloed in one chapter. The human is downloading these from the Wix site
   and will hand them over. **Waiting on those files** — nothing to build
   yet, this is a placeholder note so the next session picks it up. Kresba
   stays as-is (the one piece already recovered) until they arrive.
3. **The chronicle's heading and scope.** Disliked "Co jsme psali, a co jsme
   přestali psát" and wanted it to read like the real Aktuality feed, with
   real photos, not a curated 9-line highlight reel. Confirmed with the
   human: full real-feed treatment, heading just "Aktuality," and — since
   they separately said they loved the courses rail and wished more of the
   page could scroll sideways — built as a wide `pan` rail rather than a
   vertical list. See the full rebuild below.
4. **Course cards: "Děti" and "Dospělí" read as generic, not aikido-specific.**
   Píďata and Jóga were fine as named. Changed to "Aikido děti" and "Aikido
   dospělí."
5. **The close felt sterile.** Added a real photo (the sensei-and-kids camp
   photo, `images/o-nas-main.png`, already recovered but unused) as a second
   column beside the closing text, within the grammar's masthead-close rules
   (no spotlight, no magnet, CTA still a line of running text).
6. **Wants more of the previous site's texture generally.** Addressed
   directly by rebuilding Chapter II around the real archive rather than
   inventing new copy: this is the single biggest lever for "feels like the
   old site" without breaking the taste floor's ban on invented content.

## The Aktuality rebuild

Went back to the actual Wayback Machine archive again, this time for real
event photography rather than a comic. The Wix-era photos referenced in
`data/aktuality.json` are mostly tiny (embedded at 130–250px wide, Wix's own
fill-crop URLs, no larger cached variant found), too low-resolution to use
at card size without looking soft against the taste floor's quality bar. The
**pre-Wix site (2006–2017, hosted directly on `aikidoricany.cz/img/`)**
turned out to have full-resolution originals archived alongside the
thumbnail ("s"-suffixed) versions the old page actually displayed — the
thumbnails are what's in `aktuality.json`, but the full files are still
there under the plain filename. Pulled six from that trove after checking
each one's actual content and resolution:

| Year | File | Real resolution | What it shows |
|---|---|---|---|
| 2011 | `kolace-2011.jpg` | 640×480 | Koláč-contest winners, group photo |
| 2012 | `kolace-2012.jpg` | 2000×1500 | A wooden spoon handed to sensei; paper cranes in the window |
| 2013 | `staz-2013.jpg` | 2000×1523 | A visiting sensei teaching a child, full dojo mid-session |
| 2014 | `vyroci-10let-2014.jpg` | 1504×1000 | 10th-anniversary formal seiza line-up |
| 2014 | `kolace-2014.jpg` | 676×900 | Kids and a koláč, bokken/jō rack on the wall |
| 2015 | `svycarsko-2015.jpg` | 2480×483 | Panoramic group photo, international seminar in Switzerland under sensei Hiroshi Tada, the club's own torii banner visible on a hung sign |

All saved to `images/aktuality-archiv/` in the main project, not just this
build. Real post text for the remaining beats (2018 Baionšómjó return, a
2022 city grant, 2025 today) fills the chapter to the present without a
photo where none survived at usable resolution. Three of the four
previously-"lost" activity cards (Ha Tha Jóga, the singing retreat,
Meditace/Óm/pránajáma, Tchaj-ři čchüan) are kept in the rail, dated at their
real era, marked `zmizelo z webu`, but no longer the chapter's main frame —
now they're a few cards among many, not the whole point.

**New signature move: coming into focus.** The old tally (a live count of
kept-vs-lost) doesn't fit a full real-feed rail — there's no longer a small,
countable "lost" set to tally against a countable "kept" set in the same
way. Replaced with a different bespoke mechanic that keeps the same honesty:
the recovered activity cards sit blurred and faded by default and sharpen to
full clarity only as they cross the horizontal centre of the viewport,
reading real `getBoundingClientRect()` position every frame the act is in
view. Every other card in the rail is always fully legible; these are the
ones you have to actually scroll to and look at, which is the literal truth
of how they were found — dug out of an archive, not sitting on the surface
like the rest of the feed.

## Fourth revision: the real files arrived

The human uploaded the actual Wix source export to `wixsite,pdfs,imgs/` in
the project root: a `komiks/` folder (the four comics, full pages plus
separate profile portraits, as raw scans) and a `fotky/` folder (real event
photography by trip/occasion, far more than was ever pulled into
`aktuality.json`).

**The comics, identified and fixed up:**

| Colour | Character | Full piece | Profile portrait |
|---|---|---|---|
| Yellow | Boy with origami | Multi-panel strip (already known, now from a clean unwatermarked source) | `origami dítě_edited.jpg` |
| Red | Geisha with a rose | Multi-panel strip, same beat as yellow: a blow lands and she's simply turned aside | `gejša s růží_edited.jpg` |
| Grey | Old man with a butterfly | Multi-panel strip, calmest of the four | `děda s motýlem_edited_edited_edited.jpg` |
| Blue | Samurai | Single full-page portrait, not a panelled strip | `samuraj_modrý_edited.jpg` |

All four raw scans were sideways (rotated 90°, two different directions) and
enormous (up to 8266×5844, 21MB). No ImageMagick or Python on this machine,
so processed them with .NET's `System.Drawing` via PowerShell instead:
rotation determined by trial (render, check, correct), then downscaled to a
sane web size and re-encoded as JPEG. Saved to `images/komiks/` in the main
project (8 files: 4 full pieces + 4 profile portraits) and copied into the
build. Every one carries the same "PF 2003" signature, so the chapter is now
dated to that year rather than left vague.

**Kresba, rebuilt to show all four, not just one.** It couldn't become a
third `pan` act (it sits between Aktuality and Pro koho, both already `pan`,
and a third would repeat the device twice in a row). Instead it's a plain
CSS horizontal scroller inside its `flow` section — genuinely side-scrolling,
which the human said they wanted more of, without touching the engine's
device-variety rule. Each card pairs the full artwork with its round profile
portrait and a one-line caption naming the beat: every one of the four
follows the same shape as the origami page, force met with redirection or
simply stepping aside, never a clash won outright.

**Added to Aktuality too**, per "add them to all the posts": a new opening
2003 card (the earliest date on the page now, predating even the first
Wayback capture) uses the yellow piece as its photo and points down to
Kresba for the rest. The Aktuality lead paragraph's year range updated from
2006 to 2003 accordingly.

**One photo pulled from `fotky/` for the real feed's ending.** The 2025
closing card was text-only; `fotky/italia25/` had real, current, high-
resolution photos from the actual summer trip. Used one: two dojo members
kneeling beside their host sensei in Italy, a portrait of O-Sensei Ueshiba
behind them. The rail now opens and closes on a real photograph. Did not
mine the rest of `fotky/` (10let, primestsky tabor, aikivandr, vanocni čaj,
etc.) — there's clearly more real material in there for future posts, but
this pass covered the two things the human asked for.

**A CSS specificity bug found and fixed along the way**: the profile
portraits initially rendered at full card width instead of as small round
avatars, because a broader `.komiks-card img` rule (one class + one element,
higher specificity) was beating `.komiks-card__avatar` (one class). Fixed by
scoping the broad rule to `.komiks-card > img` (direct children only) so it
can no longer reach the nested avatar at all.

## Fifth revision: all of it, verbatim

The human's instruction was direct: every real post, verbatim, not a
curated 15-card selection. Regenerated Chapter II from `data/aktuality.json`
programmatically (66 entries, reversed to chronological order, original
HTML preserved as-is: bold, links, prices, ALL-CAPS emphasis, the informal
voice, unedited) plus the 3 real "lost activity" excerpts pulled verbatim
from `historie.html` (Ha Tha Jóga, Meditace/Óm/pránajáma, Tchaj-ři čchüan)
and the 2003 comics card. 69 cards total, all real, none paraphrased.
`data-sc-span` raised from 5.6 to 26 to match. Total page length is now
~36.6 viewport-heights, far past any budget this skill would otherwise set,
which is the direct and accepted cost of "all of it" over "a curated
edit." Verified clean on desktop, mobile, and reduced-motion: no dead
scroll, all text clears 4.5:1 contrast.

## Sixth revision: wireframe first, then a different shape entirely

After the full-verbatim pass, the human asked to stop and wireframe before
another full rebuild. Audited all 13 original pages against the 7 chapters
and found real gaps the human had already named: no Rozpis hodin, no proper
Kontakt, no Přihláška, no Galerie, thin course copy, one CTA at the very
end. Published a content-map artifact with the gap list and a recommended
architecture (scroll page as front door, existing pages handle the
transactional content) for sign-off before touching code again.

The human then asked for everything on that map, **and** a structural
change: horizontal between chapters, vertical inside them (their words:
"whole kronika can be scroll down, most recent on top"), and separately, to
cut butterflies out of the grey comic and animate them across the screen on
scroll.

This is not a variation on chaptered editorial. It's `#hub`: a native CSS
`scroll-snap-type: x mandatory` row of eight full-viewport slides (Domů,
Cesta, Aktuality, Kresba, Pro koho, Příspěvek, Galerie, Kontakt); each slide
is independently `overflow-y: auto` so a chapter with more content than
fits one screen scrolls on its own vertical axis without moving its
neighbours. The scrollcraft engine (pin/pan/reveal/cue) is built for a
single vertical document and doesn't model this shape, so it's gone from
this build entirely — plain CSS scroll-snap plus a small amount of bespoke
JS (active-slide detection for the nav chrome's colour and the dot
indicator, smooth-scroll-to on click). `shoot.mjs` doesn't understand this
page either; verified instead with a purpose-built Playwright script that
walks all eight slides and one deep vertical scroll into Aktuality.

**What filled the gaps:**
- Aktuality's 66 verbatim posts, re-ordered newest-first (not reversed
  anymore — this is the JSON's own native order), file/photo links inside
  post text styled as bordered chips so they read as the buttons they were.
- Pro koho: full verbatim paragraph per course (from
  `data/site-content.json`, not the one-line teaser), plus a real CTA row
  to Rozpis hodin and Přihláška.
- Příspěvek: the real period pricing (2 800 Kč/pololetí, 5 100 Kč/školní
  rok) and the real discount tiers (20 % sourozenci/děti členů/důchodci a
  studenti, Start Na Cestě −20 %) from `cenik.html`, framed as recommended
  contribution tiers rather than a discount off free.
- New Galerie slide: the 4 real YouTube videos and one representative photo
  per real gallery category (7), linking out to the full `galerie.html`.
- Kontakt rebuilt in full: real embedded map, instructor name, socials, the
  2 PDF application downloads, a mailto CTA.

**The butterflies.** Cropped three individual butterflies out of
`images/komiks/komiks-sedy.jpg` (the grey "děda s motýlem" comic) with
`System.Drawing` — no Photoshop or segmentation tool on this machine, so
found clean crops on flat background by trial, then ran a per-pixel
luminance threshold to cut real alpha transparency (not a blend-mode
trick, so they read correctly on both light and dark slides). They drift
continuously via a single `requestAnimationFrame` loop, nudged by however
far you've scrolled — both `#hub.scrollLeft` and whichever slide's own
`scrollTop` is currently active feed into the same drift formula, so the
motion responds to both scroll axes at once. `prefers-reduced-motion`
removes them entirely rather than freezing them mid-flight.

## Grammar (historical — see the note above; this build no longer uses it)

**Chaptered editorial** (references/uniqueness.md §2.2). The other seven:
*filmic one-shot* is the default drift and this brief is explicitly not one
continuous carried argument, it's the club's own record across three visibly
different eras — a film would paper over exactly the discontinuity that's the
point. *Live surface* needs a real running product; there isn't one. *Continuous
world* requires worldflight and one unbroken place; the brief's own answer to
Q7 was distinct scenes. *Typographic poster* fits a brand whose only asset is a
sentence; this brand's asset is twenty years of real photographs and a real
lineage, and leaning on type-only would waste them. *Gallery/catalog* fits a
range where the visitor's question is "what are the options"; that's true of
one chapter (courses) but not the whole page. *Split stage* needs a two-sided
argument; nothing here is a comparison. *Rhythmic cutlist* fits an energy
brand; "nenásilná cesta" and the family/non-commercial steer are the opposite
of a pulse-first page. Chaptered editorial is the one grammar built for
long-form substance with hard cuts between distinct grounds, no fixed bar, and
real figures inside prose — which is exactly what a 20-year archive and four
real courses are.

No video footage exists in the project and ffmpeg isn't installed on this
machine, so the build uses zero `scrub` acts (the grammar allows up to one;
zero is inside that). Every act is photographic and driven by real images
already in the repo.

## Signature move

**The tally.** Chapter II prints nine real, dated chronicle entries as the
reader scrolls: five posts that are still true today, four activities
`historie.html` found had quietly disappeared from the site (Ha Tha Jóga,
Prožitkové zpívání, Meditace/Óm/pránajáma, Tchaj-ři čchüan), each marked
`zmizelo` and left dashed rather than cut. Alongside the list, a small live
ledger in the corner counts both totals up in real time, in sync with
whichever entries have actually arrived, landing on the true 5/4 split by the
time the act ends. It reads its own entries' cue thresholds directly off the
DOM each frame rather than animating toward a pre-set target, so the count
can never drift out of sync with what's on screen, which is the difference
between this and reaching for the kit's `count` device: `count` animates one
number to one fixed target once, this recomputes two live numbers from
markup, continuously, for as long as the act is in view. Only real figures,
both independently checkable against `content/pages` and `historie.html`.

## Fingerprint gate

Registry (`scrollcraft/FINGERPRINTS.md`) is empty — first build in this
workspace, nothing to clear. Passes by definition. Row appended after
shipping and verifying.

## Score table

| Chapter | Device | Why this one |
|---|---|---|
| Title page (no number) | `flow` + `in`, type only | Chaptered editorial's hero is a title page, not a hero shot — mark, name, "nenásilná cesta" on plain paper ground, media starts in Chapter I |
| I · Cesta (the way) | `reveal` (up) on the real throw photo, `flow`+`in` on the ai/ki/dó text | A wipe is a change of state, which fits "here's what this actually is" better than a plain cue; media in its own column with a caption, not full-bleed |
| II · Aktuality (the peak) | `pan` rail, 15 real archive posts, mixed photo/text/wide cards + bespoke focus-on-centre for the recovered ones | The richest, densest chapter earns the peak; a wide rail is also the direct answer to "more side-scrolling" |
| III · Kresba (the comic) | `flow`+`in` only, no wipe | A quiet breath after the dense archive rail and before the next one; deliberately undramatic so the image is the moment, not the device |
| IV · Pro koho (courses) | `pan` rail, 4 items (Píďata → kids → adults → yoga), museum-label schema (age, one line) | Lateral travel reads as a range of doors in, not a hierarchy; matches "pick your age, pick your door" |
| V · Příspěvek (the fee) | `flow`+`in`, real figures stated plainly (0 Kč floor, 800 Kč recommended) | No hero-metric card, no discount headlined next to "it's free"; only real numbers, per the brand's own no-invented-stats rule |
| Colophon (close) | `flow`/`pin`, small type, real photo in a second column, CTA as a line of running text | Chaptered editorial's close is a masthead plate, not a pinned spotlight+magnet island (both banned); the photo answers "feels sterile" without breaking either rule |

Four device families (`flow`/`in`, `reveal`, `pan`, `pin`); no family repeats
back-to-back — the two `pan` rails (II and IV) sit on opposite sides of
Kresba's plain `flow`+`in` specifically so they never touch. Zero `scrub`
acts. Total length ≈16.2 viewport-heights across 7 units — well past the
8–14 budget, which is the direct, acknowledged cost of building the full
real archive as a rail instead of a curated shortlist; paid deliberately on
explicit request, not cut to fit.

## Verification (Step 5)

Ran `doctor.mjs` first: node and Chrome present, ffmpeg missing, no
KIE_AI_API_KEY. Both are irrelevant to this build (zero `scrub` acts, no
generated assets), noted rather than worked around.

`shoot.mjs` run three times (desktop 1440×900, mobile 390×844,
`--reduced-motion`) against the first build (the sediment-stack version),
fixing real defects between runs rather than tuning until a report looked
clean:

- **Contrast, normal motion.** The sediment note's white text sat directly on
  whichever era screenshot was behind it, unshielded, and failed as low as
  1:1 against era2/era3's pale Wix backgrounds. Root cause was two bugs: an
  empty scrim div collapsing to a sliver instead of covering the text's real
  height, and a scrim that carried its own `data-sc-cue`, which the
  verification pass hides along with the text it exists to protect while
  measuring what's behind it. Fixed, then the whole approach was replaced.
- **Contrast, reduced motion.** Same family of bug on the lead heading's
  corner scrim. Fixed, then replaced along with the rest of the chapter.
- **Toolbar bleed / folio-rail collision:** both fixed at the time (crop via
  oversized static offset; rail cards given vertical margin) and both
  findings still hold in the rebuilt page, since Chapter III and the folio
  chrome didn't change.

Chapter II was then rebuilt from scratch on human feedback (the sediment
stack was cut, replaced with the real chronicle and tally). Re-ran all three
`shoot.mjs` passes against the rebuilt page:

- **Dead scroll:** none, on any of the three runs.
- **Contrast:** all cues clear 4.5:1 at their worst frame, on all three runs.
  The chronicle entries sit on a flat navy ground rather than over
  photography, so the whole scrim/hidden-cue failure class this chapter hit
  before doesn't apply here at all.
- **"Never peak":** gone. The old sediment note's single slow-arriving cue is
  replaced by nine ordinary entry cues that each hold once they arrive, and
  the harness's own per-frame cue counts (1, then 3, 5, 7, 8, 9 as the reader
  scrolls) confirm the accumulation is landing exactly as designed.
- Contact sheet: still skipped, ffmpeg is a stripped build on this machine
  (no `scale`/`tile` filters). Verified by reading the individual frame PNGs
  in `lab/shots`, `lab/mobile`, `lab/reduced` directly instead.

## Feel check

Scrolled the finished page cold and wrote one word per act before diffing
against the intended curve in the table above:

| Act | Felt | Intended | Match |
|---|---|---|---|
| Title | quiet | quiet, grounded | yes |
| I · Cesta | settling | small release | close: reads as calm rather than a release specifically, acceptable |
| II · Kronika | struck, honest | quiet pride, honesty | yes, the strongest moment on the page; the dashed "zmizelo" entries land harder than the sediment version did |
| III · Pro koho | welcoming | clarity, welcome | yes |
| IV · Příspěvek | plain, trusting | trust, openness | yes |
| Colophon | resolved | warm invitation | yes |

The peak holds: largest span on the page (4 of the ~13.4 total), the tally is
the only bespoke interaction on the site, and the close resolves on a real
sentence and real contact details rather than trailing off.

## Authored silence

The pause between the philosophy act settling and the chronicle heading
surfacing is deliberate — a beat of empty navy ground before the first entry
lands, not dead scroll. Flag it as intentional during verification.
