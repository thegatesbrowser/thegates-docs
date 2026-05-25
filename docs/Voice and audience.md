---
tags: [voice, audience, conventions]
---

# Voice and audience

The single most common failure mode for new pages in this repo is
writing in the **wrong voice for the wrong reader**. Read this before
drafting any page.

## Audience priority

Per `CLAUDE.md` at the repo root, in this order:

1. **Gate creators** — Godot developers shipping a world. Most pages
   serve this reader. Pragmatic, code-aware, evaluating whether to
   invest time.
2. **End users** — curious visitors deciding whether to install. The
   Introduction page, FAQ, and Security overview are for them.
3. **Contributors** — people who want to work on the engine itself. The
   Community section is their door.

But there's a sharper version of this, learned from research and from
inspecting the actual product surfaces:

**The docs are primarily for creators.** The main `thegates.io` site
and the app's own in-app onboarding (the Welcome hub, the search bar)
handle the visitor experience. A visitor who lands on `docs.thegates.io`
is usually arriving via search with a specific question — they don't
need a sales pitch. They need an answer.

This is consistent with how Godot, Tauri, Bevy, and htmx all structure
their docs: developer-first, with thin visitor-orientation as context.
None of those projects have a separate "About" pillar. See
[[Site structure]] for the comparison.

## The two voices in the wild

There are two distinct marketing surfaces for TheGates, with
**deliberately different voices**. Don't mix them.

| Surface | Voice | Example |
|---|---|---|
| `thegates.io` | **Aspirational, philosophical.** Capitalized "Digital Worlds" / "Web Pages" as if brand terms. Audience: anyone, but biased toward the visitor / believer. | *"Building a New Internet More Interactive, Social and Fun. We are building a new 3D internet, where instead of scrolling Web Pages you can dive into beautiful Digital Worlds."* |
| `thegates.io/export-plugin` | **Pragmatic, benefit-focused.** Concrete verbs. Audience: a Godot dev. | *"Publish your Godot project with just One Click. Instantly publish your Godot projects. Share with players, gather feedback, and deploy updates instantly across Linux, Windows, and macOS."* |

**The docs match the export-plugin voice.** Not the main site voice.
The reason: the docs are the technical companion to whichever pitch
brought the reader here. Recreating the main-site pitch in the docs
would either (a) feel redundant to someone who just came from
`thegates.io`, or (b) confuse someone who came from a Discord link or
search result without context.

When the Introduction page needs to acknowledge the broader vision,
it points at `thegates.io` and gets out of the way:

> *"For the broader vision, see thegates.io — these docs are about how to build."*

## Voice rules (from CLAUDE.md, never violate)

These are repeated here because they're load-bearing:

1. **Headers must pass the scan test.** Reading just the headers should
   deliver the page's argument. Avoid meta headers like *"How it
   works"*, *"What this means"*, *"Recommendation"*. Headers are
   **claims, not labels.**
   - Bad: *"Safety"*, *"Why TheGates"*, *"Vision"*.
   - Good: *"Sandboxed by default"*, *"Built on Chromium"*, *"What gates
     can't reach"*, *"Trust gates like websites"*.
2. **Lead with honesty, then confidence.** Security pages do this well
   — the *"v1.0 ships the foundation of our sandboxing. We'll keep
   strengthening it as the platform grows"* note appears in the first
   paragraph, not buried. Copy the pattern.
3. **No emojis** in new prose. Preserve existing emojis in legacy pages
   only if asked.
4. **No marketing speak.** No *industry-leading*, *next-gen*, *unlock
   the power of*, *spark a new ecosystem*, *fuel the next wave of
   innovation*. If a sentence could appear on any 3D-platform's docs
   site, rewrite it so it could only appear on TheGates'.
5. **No personal anecdotes.** Lines like *"After we'd built the initial
   prototype, I found out..."* belong on a blog, not in product docs.
6. **Cross-link aggressively with `:doc:`.** Pages should not be
   islands. Add a `See also` block at the end of every page that points
   at the natural next reads.
7. **RST line blocks (`| ...`).** Match the existing pattern.
   `index.rst` and `security/overview.rst` are good references.

## The boundary between this vault and the engineering vault

Engineering knowledge — the C++ classes, file paths inside the code,
build flags, syscall numbers, SBPL fragments — lives in the parent
vault (`../thegates/docs/` and `../thegates/godot/notes/`). The public
docs **lift concepts, not engineering prose**.

| Lift freely | Never lift |
|---|---|
| Conceptual architecture (two-process model, shared GPU texture, per-gate isolation) | Function names, file paths inside the codebase, build flags (`TG_RENDERER`, scons options) |
| Public-facing tech names (Chromium sandbox, Godot Engine, Wayland, AppContainer, Seatbelt, Landlock, seccomp) | Syscall numbers, BPF or SBPL fragments, ACL syntax |
| The headline framing (*"Browsers sandbox tabs. We sandbox worlds."*) | Internal IPC command names beyond what gate creators need to call |
| Honest trust calibration (*"hardening layer, not a guarantee"*) | Specific sandbox loopholes or attack-surface enumeration |
| | "Future Work" / roadmap content unless explicitly cleared for public |

If you find yourself naming a C++ class or a Sphinx-side debug option
in a page meant for gate creators, you are over-lifting. Translate it
to user-facing language.

## How to write a page in this voice (the recipe)

1. **Decide one reader.** Creator, visitor, evaluator, contributor —
   pick one. If you can't, the page is doing too much; split it.
2. **State the page's one job in a sentence.** Out loud. If you can't,
   the page is unfocused.
3. **Write the headers first as claims.** Each header should be a small
   true sentence about the section's content. Reading only headers
   should give the page's argument.
4. **Write the lead.** First paragraph. Should answer: what is this
   page about, who is it for, what will I know after reading it.
5. **Fill in content under headers.** Concrete > abstract. Examples >
   prose. Tables when comparing things. Code blocks for code.
6. **Add `See also`.** Two to four `:doc:` links to natural next reads.
7. **Re-read against the rules above.** Cut anything that fails them.

## Pitfalls observed in the current docs

Patterns that show up in the existing About / Concepts pages and
should never be repeated:

- **Confused audience.** `about/introduction.rst` tries to talk to
  visitors and creators in the same paragraphs. Result: useful for
  neither.
- **Label headers.** Same file: *"What is TheGates?"*, *"Safe by
  design"*, *"3D Internet"*, *"Why it matters"*, *"Vision"*. None of
  those tell you anything when scanned.
- **Marketing prose.** *"This shift will spark a new ecosystem of
  internet projects and fuel the next wave of innovation."* That is the
  exact prose CLAUDE.md forbids.
- **Personal anecdote.** *"After we've built the initial prototype, I
  found out..."* That belongs in a blog post.
- **Repetition across pages.** The sandbox story and the two-process
  story currently appear in 4-6 different pages. Each fact should live
  in exactly one canonical page; other pages link to it.
- **Generic analogies.** *"Ready Player One"* — informal, doesn't earn
  its place. If the analogy could apply to Decentraland, Roblox, or
  Hytopia, it's not specific enough.
- **Emojis.** 🌌 and ✨ on the current Introduction page.

## Quick checks before you ship a page

- [ ] One reader. Named.
- [ ] One job. Statable in one sentence.
- [ ] Headers are claims. Scan test passes.
- [ ] No marketing words. No emojis. No personal anecdotes.
- [ ] No engineering jargon a creator wouldn't recognize.
- [ ] Cross-links to natural next reads at the bottom.
- [ ] If a fact appears here that also appears on another page, decide
      which page owns it and `:doc:` from the other.

## Sources

- `../../CLAUDE.md` (this repo's agent contract — the canonical rule
  set).
- `../thegates/CLAUDE.md` (parent project's contract — parallel voice
  conventions).
- [thegates.io](https://thegates.io) — main marketing voice in the
  wild.
- [thegates.io/export-plugin](https://thegates.io/export-plugin) —
  pragmatic voice in the wild (this is the voice docs should match).
- Comparison research distilled in [[Site structure]].
