---
tags: [meta, moc]
---

# Index — agent knowledge vault for thegates-docs

You are reading the entry point for **anyone (human or AI agent) working on
the `thegates-docs` repo**. This is not the public documentation — the
public docs are the `.rst` files at the repo root (`about/`, `concepts/`,
`getting-started/`, etc.). This `docs/` folder is the *context layer* you
read **before** you touch those `.rst` files.

If you're an AI agent and you've been told "read `docs/` before working on
this repo", you've already done the right thing. Read everything in this
folder once per session before you start editing. It takes ~10 minutes.

## Read in order

1. **[[The project]]** — what TheGates actually is, end-to-end. The
   launcher, the gate format, the v1.0 sandbox, the backend, the ecosystem.
   Without this, you'll write docs that are conceptually wrong.
2. **[[Voice and audience]]** — who reads the public docs, what voice they
   should hear, and the deliberate split between `thegates.io`
   (aspirational) and `docs.thegates.io` (pragmatic). The single most
   common failure mode is writing in the website's voice.
3. **[[Site structure]]** — the six-pillar sidebar, what each pillar is
   for, the current pages and their known problems, and the patterns
   we lifted from other docs sites (Godot, Tauri, Bevy, htmx, Stripe,
   Decentraland).

## Source-of-truth boundaries

This vault is the **public-docs-facing** layer. It deliberately does NOT
duplicate the engineering source of truth. When you need deeper technical
ground truth, go to the parent vault:

- **`../thegates/docs/`** — main project vault. Architecture, two-process
  model, gate format, launcher, gotchas. Start at `../thegates/docs/Index.md`.
- **`../thegates/godot/notes/`** — engine fork notes. Sandboxing, custom
  Godot module, external texture sharing. Start at
  `../thegates/godot/notes/Index.md`.
- **`../thegates/CLAUDE.md`** — the contract for AI agents working on the
  engine project itself. Voice and conventions parallel ours.

Both parent folders are one Obsidian vault when opened from `../thegates/`.
Wikilinks resolve across them. **You can lift concepts freely — never lift
engineering prose** (class names, file paths inside the C++/GDScript code,
build flags, syscall numbers, SBPL fragments). See [[Voice and audience]]
for the rule.

## Conventions in this vault

- Every page has frontmatter with at least `tags:`.
- Wikilinks (`[[Page name]]`) for cross-references inside this vault.
- Markdown links (`[text](url)`) for external URLs.
- Relative file paths (`../thegates/docs/Foo.md`) when pointing at the
  parent vault.
- Sources are listed inline next to claims, not in a footnotes section.
- Voice matches the parent vault: terse, opinionated, examples > prose.
  No marketing speak ever.

## What this vault is NOT

- Not the public docs. Don't put user-facing prose here.
- Not a planning area. Plans live in `RESTRUCTURE_PLAN.md` (transient) at
  the repo root, or in TODOS.md (durable deferred work).
- Not a personal scratchpad. If a fact wouldn't help another agent, don't
  write it.
