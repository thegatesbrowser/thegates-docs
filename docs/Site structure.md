---
tags: [structure, ia, conventions]
---

# Site structure

The shape of the public docs site and the reasoning behind it. Read
this before adding, renaming, or moving any page — the toctree in
`index.rst` is more deliberate than it looks.

## Build stack

- **Sphinx** + **Read the Docs theme** (`sphinx_rtd_theme`).
- Hosted on Read the Docs.
- Source: [github.com/thegatesbrowser/thegates-docs](https://github.com/thegatesbrowser/thegates-docs).
- Published at [docs.thegates.io](https://docs.thegates.io).
- Build: `make html` (or `make clean && make html` when the toctree
  changes — incremental builds don't propagate sidebar changes to
  already-built pages).
- Live preview: `sphinx-autobuild . build/html` then open
  `http://127.0.0.1:8000`.

## The intended sidebar shape

Six pillars. Order matters — the sidebar is the implicit reading order
for someone going top-to-bottom.

| Pillar | Job | Primary reader |
|---|---|---|
| **About** | Lean on-ramp. *"What is this thing, briefly."* + FAQ. Hand off to Get started. | Creator arriving with no context. |
| **Get started** | The happy path from zero to a published gate. Quickstart, hosting, linking, GDExtension, troubleshooting. | Creator about to ship. |
| **Security** | The trust story. Sandbox model, per-gate isolation, network policy, Wayland/X11, how to verify. | Safety-curious reader (creator or end user). |
| **Architecture** *(new — see [[#Restructure in progress]])* | The under-the-hood model. Two processes, shared GPU texture, per-gate engine version, cross-platform sandbox enablement. | Technically-curious creator. |
| **Reference** | Lookup-style: the `.gate` file spec, command channel. | Creator looking up a field. |
| **Community** | Where to find help, contribute, follow updates. | Anyone who needs people. |

**Audience tightens, then opens.** About is mixed (creator-leaning).
Get started and Architecture are creator-only. Security and Reference
span both creator and evaluator. Community is everyone.

## Restructure in progress

A restructure of About + Concepts → About + Architecture is being
executed. The state of that work and the rationale lives in
`../RESTRUCTURE_PLAN.md` (transient — delete after execution). High
level:

- **Delete the `concepts/` pillar.** Its strongest page (the
  two-process / how-it-works architecture) becomes the seed for a new
  **Architecture** pillar between Security and Reference. The other two
  Concepts pages distill into one-liners on the new Introduction or get
  cut.
- **Lean the About pillar.** Introduction becomes a 30-second
  orientation with a screenshot anchor. FAQ regrouped by reader.
- **Stamp out repetition.** Sandbox and two-process facts currently
  appear in 4-6 pages. After the restructure, each lives in one
  canonical place; others link to it.

When the restructure ships, update this page to reflect the final
shape.

## Each pillar today, in detail

### About

`about/introduction.rst`, `about/faq.rst`. **Currently mixed-audience
and over-padded** — both pages are scheduled for full rewrites in the
restructure (`../RESTRUCTURE_PLAN.md`). Once rewritten:

- Introduction = one screenshot, one tight definition, one paragraph
  on what you ship, two paths forward. ~150 words.
- FAQ = grouped by reader (Creators / Trust and safety / Visitors),
  short answers, deep `:doc:` links.

### Get started

`getting-started/quickstart.rst`, `hosting.rst`, `linking-gates.rst`,
`optional.rst`, `troubleshooting.rst`. **Considered good.** Don't
restructure without an explicit reason. Voice is direct, steps are
numbered, screenshots exist (`getting-started/img/`).

### Security

`security/overview.rst`, `per_gate_isolation.rst`, `network_policy.rst`,
`wayland_and_x11.rst`, `verify_the_sandbox.rst`. **Considered good.**
The Overview opens with the headline framing *"Browsers sandbox tabs.
We sandbox worlds."* and uses Sphinx tabs to show the per-OS shape.
This is the voice model for the rest of the site.

The v1.0 sandbox is a real engineering achievement (see [[The project]]
§ "v1.0 sandboxing"). The current docs cover it well but could lean
into the cross-platform unified architecture more confidently — that's
a future polish, not a restructure.

### Architecture (new pillar)

`architecture/overview.rst`. Single page at launch, will grow if
creator demand justifies. Receives content from the deprecated
`concepts/how-it-works.rst` plus the engine-version-stability section
from the deprecated `concepts/what-is-a-gate.rst`. Sits between
Security and Reference because it shares context with both (Security =
*why* the sandbox; Architecture = *what enables it*).

### Reference

`reference/gate_file.rst`, `reference/command_channel.rst`. **Considered
good.** Spec-format pages with Concept / Format / Fields / Example
sections. Warning callouts where needed.

One small clarification scheduled in the restructure: the
`discoverable` field's description currently reads *"if true, the
world can be indexed"* — silent on *by what*. After the rewrite:
*"indexed by TheGates' search backend (Meilisearch-powered), visible
to users typing in the in-app search bar."*

### Community

`community/contribute.rst`, `community/community.rst`. **Considered
good.** Channel list with the *"fit your need"* framing. Discord,
GitHub, Twitter, email, lnk.bio. Use this page's voice as a model for
any future utility page.

## index.rst (the home page)

Does three jobs:
1. Defines TheGates (lede + tagline).
2. Routes by audience ("Choose your path" — currently three columns;
   the restructure collapses to two: "Build a gate" and "Contribute",
   with a one-line visitor callout pointing at `thegates.io`).
3. Surfaces v1.0 news + community CTAs.

The toctree at the bottom owns the sidebar. When you add/rename/move a
page, update `index.rst` AND run `make clean && make html`.

## Deferred pages (in TODOS.md)

Things drafted or considered but held back from v1.0:

- **Recipes section** — short task-focused how-tos between Quickstart
  and Reference. Held back until there are 5+ recipes worth shipping.
  Drafts exist in git history (commit `c323035` had a `recipes/`
  directory).
- **Best practices page** — five tips from internal docs. Overlapped
  with existing pages; revisit when there's a clearer story.
- **Discover / showcase page** — waiting for a curated gate list.
- **Roadmap page** — waiting for post-v1.0 roadmap concreteness.
- **Changelog page** — start with v1.1.

See `../TODOS.md` for the durable list.

## Patterns we lifted (from other docs sites)

Research distilled from looking at how known-good docs sites handle the
*pre-Get-Started* experience. None of these projects has a separate
"About" pillar — all integrate orientation into the Get Started / Learn
flow or embed it in the home page.

| Project | What they do | What we lift |
|---|---|---|
| [Godot](https://docs.godotengine.org/en/stable/) | Home page segments by experience level (4 user profiles). "Introduction" is a chapter inside Getting Started, six pages in linear arc: orient → equip → philosophize. | Each page has one job in a sequence. Section reads top-to-bottom as a story. |
| [Tauri](https://v2.tauri.app/start/) | Tight definition first sentence. *"Tauri is a framework for building tiny, fast binaries for all major desktop and mobile platforms."* "Why Tauri?" embedded as a subsection of the Start page. No separate About. | First sentence does heavy lifting. No standalone "Why" page. |
| [Bevy](https://bevy.org/learn/quick-start/introduction/) | "Introduction" is the first page of Learn. Opens with *"If you came here because you wanted to learn how to make ___, you came to the right place!"* Explicit stability warning up front. | Lead with the reader's purpose. Be honest about scope and maturity. |
| [htmx](https://htmx.org/docs/) | First sentence is concrete comparison: *"htmx is a library that allows you to access modern browser features directly from HTML."* Embeds philosophy in functional explanations rather than a separate Why page. | Concrete > philosophical. Show the model, don't preach it. |
| [Stripe](https://docs.stripe.com/get-started) | Value → outcomes → tech steps → support, ordered on one page. Soft audience segmentation through ordering, not hard splits. | Don't force "choose your path" — order content so the reader self-selects. |
| [Decentraland creator docs](https://docs.decentraland.org/creator/) | Opens with *"All creators are welcome!"* Then segments by **what you can make** (wearables / emotes / scenes), not by who you are. | Audience-by-capability beats audience-by-identity. |

The unifying lesson: **don't build a separate "About" pillar that
visitors and creators both have to navigate around.** Either bake
orientation into the home page (Tauri/htmx pattern) or make it the
first chapter of the creator-facing pillar (Godot/Bevy pattern).

For TheGates we went with a lean middle path: a small About pillar
(Introduction + FAQ) that's explicitly creator-oriented but ends with
the visitor handoff in one line.

## Hard rules when editing the site

- **RST format with line blocks (`| ...`).** Match the existing
  pattern.
- **Update `index.rst` AND rebuild with `make clean`** when toctree
  changes.
- **No emojis in new prose.** Existing ones in legacy pages preserved
  only if the user explicitly asks.
- **Cross-link with `:doc:`.** Every page ends with a `See also` block.
- **Section headers are claims, not labels.** See [[Voice and audience]]
  for the scan test.
- **Engineering jargon stays in the parent vault.** Public docs lift
  concepts, not C++ class names.

## Sources

- `../../index.rst` — current toctree, the canonical sidebar shape.
- `../../CLAUDE.md` — the rule set this page references.
- `../../TODOS.md` — the deferred-work list.
- `../RESTRUCTURE_PLAN.md` (transient) — the in-progress restructure.
- External comparison docs linked inline in the *"Patterns we lifted"*
  table above.
