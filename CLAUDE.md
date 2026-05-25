# Contract for AI agents working on thegates-docs

If you are an AI agent (Claude Code, Codex, Cursor, Copilot, anything)
about to write or edit pages in this repo, **read this file first** and
**read the linked notes before drafting**. They are short and they are
load-bearing.

## What this repo is

The public documentation website for **TheGates**, a 3D web browser
that opens Godot-built worlds via URL. Built with **Sphinx** + the
**Read the Docs theme** (`sphinx_rtd_theme`). Hosted on Read the Docs.

Audience priority, in order:
1. **Gate creators** — Godot developers shipping a world. Most pages
   serve this reader.
2. **End users** — curious visitors deciding whether to install. The
   index page, FAQ, and Security overview are for them.
3. **Contributors** — people who want to work on the engine itself.
   The Community section is their door.

## Deep context lives in `docs/`

Before editing any page, read **`docs/Index.md`**. It points you at
three short notes — *The project*, *Voice and audience*, *Site
structure* — that ground every editing decision in what TheGates
actually is, who reads these docs, and why the sidebar is shaped the
way it is. Once per session is enough. Pages written without that
context drift into generic prose that could apply to any 3D-platform
docs site, which is the exact failure mode CLAUDE.md exists to
prevent.

## Where the deep knowledge lives

This repo is the **public-voice** layer. The **engineering source of
truth** lives in the sibling parent repo at `../thegates/`:

- `../thegates/CLAUDE.md` — the main project's rules
- `../thegates/docs/` — architecture vault (Two-Process Model, Gate
  Format and Lifecycle, Architecture Overview, Renderer Process,
  Gotchas and Conventions)
- `../thegates/godot/notes/` — engine fork + sandboxing notes
  (Custom Godot Fork, Sandboxing/, Build System)

When you need to research before writing a page, the vault is the
source. Lift the **concepts**, never the **engineering prose**.

## Public voice vs internal voice

**Lift freely**:
- Conceptual architecture (two-process model, shared GPU texture,
  per-gate isolation)
- Public-facing tech names (Chromium sandbox, Godot Engine, Wayland,
  AppContainer, Seatbelt, Landlock, seccomp)
- The headline framing ("Browsers sandbox tabs. We sandbox worlds.")
- Honest trust calibration ("hardening layer, not a guarantee")

**Never lift**:
- Function names, file paths inside the codebase, build flags
  (`TG_RENDERER`, scons options)
- Syscall numbers, BPF or SBPL fragments, ACL syntax
- Internal IPC command names beyond what gate creators need to call
- Specific sandbox loopholes or attack-surface enumeration
- "Future Work" / roadmap content unless explicitly cleared for public

If you find yourself naming a C++ class, a syscall, or a Sphinx-side
debug option in a page meant for gate creators, you are over-lifting.
Translate it.

## Non-negotiable rules

- **RST format** with line blocks (`| ...`). Match the existing
  pattern — `index.rst` and `security/overview.rst` are good
  references.
- **Section headers must pass the scan test.** Reading just the
  headers should deliver the page's argument. Avoid meta headers like
  "How it works", "What this means", "Recommendation". Headers should
  be claims, not labels.
- **Lead with honesty, then confidence.** Security pages do this well
  — the maturing note appears in the first paragraph, not buried.
  Copy the pattern.
- **No emojis** in new prose. Preserve existing emojis in legacy
  pages, but don't add new ones unless the user explicitly asks.
- **No marketing speak.** No "industry-leading", "next-gen", "unlock
  the power of". Read the security pages for the voice.
- **Cross-link aggressively with `:doc:`.** Pages should not be
  islands. Add a `See also` block at the end of every page that
  points at the natural next reads.

## Sidebar / IA

The toctree in `index.rst` owns the sidebar. Current shape:

```
About                Introduction · FAQ
Get started          Quickstart · Hosting · Linking gates · GDExtension · Troubleshooting
Security             Overview · Per-gate isolation · Network policy · Wayland & X11 · Verify
Architecture         Overview
Reference            .gate file · Command channel
Community            Contribute · Community
```

See `docs/Site structure.md` for what each pillar is for and the
reasoning behind the order.

When you add or rename pages, update `index.rst` AND run
`make clean && make html` — incremental builds don't propagate
sidebar changes to already-built pages.

## Build / preview

First-time setup:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Build the site:

```
make html               # build static HTML to build/html/
make clean && make html # when toctree changes — sidebar needs a full rebuild
```

Live reload while editing:

```
pip install sphinx-autobuild
sphinx-autobuild . build/html
# open http://127.0.0.1:8000
```

## Deferred work

Anything held back from a release goes in `TODOS.md` at the repo
root with a one-line "why held back" note and the condition that
should trigger picking it up. Don't quietly forget — and don't ship
half-finished sections to make `TODOS.md` shorter.

## When the user corrects you

- **Style or voice correction** → likely repo-wide. Ask before
  canonizing the rule here.
- **Page-specific correction** → just fix the page.
- **Factual correction about the product** → fix the page, AND
  check whether the same fact is wrong in the parent vault.
  Flag it.

## When in doubt

- Patterns first, prose second. Read the relevant vault note before
  drafting, even if you've drafted similar pages before.
- If a sentence feels like it could appear on any 3D-platform's docs
  site, rewrite it so it could only appear on TheGates'.
- If you're an AI agent and an instruction here conflicts with the
  user's explicit request, the user wins. Tell them what convention
  you're departing from and why.
