---
tags: [product, overview]
---

# The project

A concrete picture of TheGates as it exists today (v1.0). Read this before
writing any user-facing doc page — if you don't know what the product
actually does, you'll write generic prose that could apply to any
3D-content platform.

## In one paragraph

TheGates is a **3D web browser**. The launcher looks and behaves like
Chrome — tabs, back/forward, address bar (`Search or type URL`), home
page with featured gates rendered as icon cards (Welcome, Starcatcher,
Earth, Luckshot, Survive the Slimes!, etc.), and a search bar
(`What are you looking for today?`) powered by a Meilisearch-backed
backend. Every gate is a Godot 4.5 project (`.pck` file) plus a small
`.gate` manifest. When you click a gate, the launcher downloads it (and
the matching Godot renderer binary for the version the gate declares),
spawns a separate sandboxed process, and shows you the world via a
shared GPU texture. v1.0 ships cross-platform sandboxing — Windows
AppContainer + Chromium broker, Linux landlock + seccomp + capability
dropping, macOS Seatbelt with the Firefox content profile. Publishing a
world is one click from Godot via the TheGates Export plugin in the
official Godot Asset Library.

That's the whole product. Everything below is detail.

---

## The launcher

The browser UI. A Godot project that ships in the launcher binary. Built
from `../thegates/godot/` (the fork) with normal flags (no `tg_renderer`
define). Visible window. Owns the desktop, input, audio, file system, and
the network broker.

### What the user sees

- **Top chrome:** tabs (multiple gates open at once), back / forward / refresh
  buttons, home icon, address bar with placeholder *"Search or type URL"*,
  hamburger menu.
- **Home / "New Tab" page:** TheGates logo in the center, a search bar
  *"What are you looking for today?"* with a Search button, and below
  that a row of featured gates as icon cards.
- **In-gate view:** the loaded world fills the content area; the top
  chrome stays.
- **Loading screen:** while the renderer binary is downloading or the
  `.pck` is loading.
- **"Not responding" overlay:** if the renderer crashes or hangs.

Reference: `../thegates/docs/Launcher App.md` for the GDScript / scene-tree
breakdown. Screenshots: `../thegates/screenshots/1-home.png` (home),
`../thegates/screenshots/2-loading.png` (loading), and
`../thegates/screenshots/3-in-game-ui.png` (a gate loaded — specifically
the Welcome hub).

### The Welcome hub

The first featured gate ("Welcome") is a 3D space the user can walk into
to discover other gates — it has portals, a robot character, a *"Welcome
to our Hub!"* greeting, and a text input for the user's name. This is
the in-app onboarding. The public FAQ already mentions it; the
Introduction page should too.

It's a real, concrete answer to *"what does this thing actually do?"* —
beats any abstract definition.

### Launcher orchestration of the renderer

Lives in `../thegates/app/scripts/renderer/`:

| File | Job |
|---|---|
| `renderer_executable.gd` | Resolves which renderer binary matches the gate's `godot_version`; downloads from the backend if missing; caches. |
| `renderer_manager.gd` | Spawns the renderer via `OS.execute_with_pipe`. Tracks PID. Kills on close. |
| `render_result.gd` | The `TextureRect` that displays the renderer's framebuffer. Owns the shared GPU texture. |
| `command_sync.gd` | Receives commands from the renderer (open another gate, ask for the texture handle, heartbeat). |
| `input_sync.gd` | Forwards launcher-captured input events to the renderer. |
| `renderer_logger.gd` / `process_checker.gd` | Capture stdout/stderr, watchdog liveness. |

Source: `../thegates/docs/Launcher App.md` and
`../thegates/docs/Two-Process Model.md`.

---

## The renderer

A Godot binary built with `tg_renderer=yes` (defines `TG_RENDERER`).
Headless-ish — has a real display server, swapchain, and Vulkan device,
but the OS window is created invisible. Each frame's pixels go into
shared GPU memory instead of being presented to the screen. Hardcoded
to Vulkan (D3D12 / OpenGL silently ignored).

The renderer:
- Loads the gate's `.pck` (`--main-pack` argument).
- Boots normally (autoloads, main scene, `_ready`).
- After `Main::setup2`, before any gate code runs, **engages the sandbox.**
- Each frame: writes pixels into the shared texture, pulls input from the
  launcher, pings heartbeat. If the launcher pipe dies, the renderer
  deliberately crashes itself.

The renderer never reaches the disk outside its per-gate folder, never
opens its own sockets (all networking goes through the launcher's
broker), and never shows its own window. The launcher provides what it
needs.

Source: `../thegates/docs/Renderer Process.md`.

---

## Gate format

A gate is **three URLs plus an implicit fourth**:

1. The `.gate` manifest (small INI-like file)
2. The `.pck` or `.zip` resource pack (the actual exported Godot project)
3. The icon image + preview image
4. *Implicit:* the renderer binary for the declared Godot version — not
   shipped by the gate; downloaded by the launcher from TheGates' backend
   the first time it's needed.

### Manifest shape

```ini
[gate]
title = "My World"
description = "..."
icon = "icon.png"
image = "preview.png"
resource_pack = "world.zip"
godot_version = "4.5"        ; "4.3" or "4.5" today
discoverable = true

[libraries]                  ; only required if you use GDExtension
windows.debug = "..."
windows.release = "..."
linux.debug.x86_64 = "..."
linux.release.x86_64 = "..."
macos.debug = "..."
macos.release = "..."
macos.debug.arm64 = "..."
macos.release.arm64 = "..."
```

- All paths relative to the `.gate` file unless absolute.
- All three OS libraries required (supply a stub if you don't actively
  support one), both debug and release.
- `discoverable = true` means **indexed by TheGates' search backend** —
  shows up to users typing in the in-app search. `false` means it stays
  out of search but anyone with the URL can still visit. There is no
  auth model in the gate format.

### Lifecycle of a gate visit

1. URL entered → launcher fetches the `.gate` manifest.
2. `.pck` + assets downloaded (or hit cache).
3. Launcher resolves which renderer binary matches `godot_version`,
   downloads if not cached.
4. Launcher allocates the shared GPU texture.
5. Launcher spawns the renderer with `--main-pack <pck> --resolution WxH
   --url <url>`.
6. Handshake: renderer asks the launcher for the texture handle; launcher
   sends it; renderer imports the handle locally — both processes now
   share one `VkImage`.
7. Renderer signals `first_frame`; launcher fades in the world view.
8. Steady state: input one way, frames + commands the other.
9. User navigates away → kill renderer, free pipes, free texture.

Source: `../thegates/docs/Gate Format and Lifecycle.md` and
`../thegates/docs/Gate Cycle.md`.

### Why each gate ships its own engine

A gate authored on Godot 4.3 might break under 4.5 — same way a webpage
written against an old browser API might break under a new one. So the
browser keeps multiple renderer binaries (one per supported Godot
version) and picks the matching one per gate. **The IPC protocol surface
(pipe names, command vocabulary, external texture format) must stay
stable across renderer versions** because old renderer binaries cached
on user machines still call the existing commands.

Today: 4.3 and 4.5 are the supported versions.

---

## The two-process model

This is the load-bearing architectural decision. It's why everything
else works.

```
┌──────────────────────────────┐         ┌──────────────────────────────┐
│  Launcher process            │         │  Renderer process (per gate) │
│  ──────────────────          │         │  ──────────────────          │
│  • Window, input, audio      │         │  • Loads the gate's .pck     │
│  • Network broker            │         │  • Renders frames            │
│  • File system access        │ spawns  │  • Vulkan only (hardcoded)   │
│  • Bookmarks, history        │ ──────► │  • Window invisible          │
│  • Spawns the renderer       │         │  • Sandboxed (per-OS)        │
│                              │         │                              │
│         imports VkImage  ◄───┼─────────┼── exports VkImage (shared    │
│                              │  handle │   GPU memory)                │
│                              │         │                              │
│         InputEvents     ─────┼─────────┼─► receive_input_events()     │
│                              │  pipe   │                              │
│                              │         │                              │
│         Commands         ◄───┼─────────┼─── send_command(...)         │
│                              │  pipe   │                              │
└──────────────────────────────┘         └──────────────────────────────┘
```

### Why two processes (not one)

Running every visited world in the same process as the browser would mean
a crash in one world crashes the browser, a hostile world could read
your browsing history, and every world would have to use the same engine
version. Splitting them solves all three:

- **Crash isolation.** Renderer dies → launcher shows "not responding" →
  kills it → navigates away.
- **Sandboxing.** The renderer process is locked down at the OS level.
- **Per-gate engine version.** Each gate gets the binary it asked for.
- **UI responsiveness.** The browser never blocks on world-load.

### The clever bit (shared GPU memory)

Browsers use IPC + bitmaps for tab compositing. TheGates uses **Vulkan
external memory** instead — both processes have a `VkImage` backed by
the same GPU allocation. The renderer writes; the launcher reads; no
CPU round-trip. The pipe only carries the *handle* to that memory, once,
at startup.

Counterintuitive direction: **the launcher allocates the shared
texture, the renderer imports it.** Do not "fix" this. The rationale
is in `../thegates/godot/notes/External Texture Sharing.md`.

### IPC channels

Three zmq `ipc://` PAIR sockets + one inherited socketpair:

| Channel | Purpose |
|---|---|
| `command_sync` | Renderer → launcher commands (asks for handle, heartbeat, opens links, requests mouse capture). |
| `input_sync` | Launcher → renderer input forwarding. |
| `external_texture` | One-shot: launcher → renderer transmission of the GPU memory handle. |
| `network_broker` | Inherited `AF_UNIX SOCK_STREAM` socketpair. All renderer socket creation + DNS, mediated by the launcher's broker thread. FDs travel via `SCM_RIGHTS`. |

Don't break the IPC protocol — old renderer binaries cached on user
machines depend on the existing command names and arg shapes.

Source: `../thegates/docs/Two-Process Model.md` and
`../thegates/godot/notes/External Texture Sharing.md`.

---

## v1.0 sandboxing

A real engineering achievement. The current public docs slightly
underplay it. One architecture across all three OSes, deny-by-default,
canary-verified.

| OS | Filesystem | Capabilities / token | Network |
|---|---|---|---|
| **Windows** | Chromium broker (per-gate ACL + UNTRUSTED IL) | `USER_LIMITED` token, alternate desktop, per-gate AppContainer profile | In-process broker via named-pipe pair; AppContainer carries no networking capability so WFP blocks every direct `connect()` at `ALE_AUTH_CONNECT`. |
| **Linux** | landlock (path allow-list) | `capset` to empty | seccomp removes `__NR_socket`, `bind`, `listen`, `connect`, `socketpair`. |
| **macOS** | Seatbelt SBPL (Firefox content profile + addend) | n/a — Seatbelt is monolithic | `(deny syscall-unix (syscall-number …))` for the 12 BSD syscalls that create or retarget network FDs. |

All three end with the same observable contract — gate cannot read user
files outside its per-gate folder, cannot reach sibling gates' folders,
cannot open a raw network socket. The renderer's `IP::resolve_hostname`
and `NetSocket` are hooked to route through the launcher's broker
instead of touching the kernel directly. Cross-platform canary
verification asserts the lockdown before any gate code runs.

The sandbox engages in `Main::setup2` — **before any gate-supplied code
runs** (GDExtension `DllMain` / `.init_array`, autoload `_init`,
main-scene `_init`, `_ready`). Native and scripted gate code share the
same threat boundary.

The launcher's in-process **network broker** mediates all renderer
networking. It opens kernel sockets on the renderer's behalf, validates
CIDR policy (private IP ranges and loopback are denied; public addresses
allowed), and hands FDs back via `SCM_RIGHTS` (POSIX) or
`WSADuplicateSocket` (Windows). No installers, no system extensions, no
setuid helpers.

Source: `../thegates/godot/notes/Sandboxing/Index.md`. Drill-downs:
`Architecture.md`, `Linux Backend.md`, `macOS Backend.md`,
`Network Isolation.md`, `Bootup Performance.md`, `GDExtension Loading.md`.

---

## The backend

`../thegates-backend/` — a Django + Meilisearch service. The launcher
talks to it for discovery, search, analytics, publishing, and renderer
binary downloads.

API endpoints (in `../thegates-backend/src/api/urls.py`):

| Endpoint | Purpose |
|---|---|
| `api/analytics_event` | Telemetry. |
| `api/create_user_id` | Anonymous user ID assignment. |
| `api/discover_gate` | Returns a single gate (URL lookup). |
| `api/featured_gates` | The icon row on the launcher home. |
| `api/all_gates` | Full list (for browsing / search). |
| `api/search` | Meilisearch query against indexed gates (those with `discoverable = true`). |
| `api/prompt` | Search prompt / suggestions. |
| `api/send_logs` | Diagnostic upload. |
| `api/upload_build` | Upload a built `.pck`. |
| `api/publish_project` | The export plugin's one-click publish endpoint. |
| `api/get_published_project` | Lookup for a published project. |
| `api/create_publishing_user_id` | Publisher identity. |
| `api/download_renderer/<platform>-<version>` | Per-version renderer binaries (the launcher fetches the matching one when it first opens a gate built against that Godot version). |

**TheGates hosts gates for free.** A creator who runs the export plugin
gets a `thegates.io`-hosted URL out of the box. Self-hosting on any HTTP
server is also supported — that's what the docs' `getting-started/hosting`
page covers.

---

## The ecosystem (sibling repos)

The project is a multi-repo workspace under `../`. Knowing what each
folder is keeps you from looking for context in the wrong place.

| Folder | What it is |
|---|---|
| `../thegates/` | **Main engine project.** The Godot fork (`godot/`), the launcher app (`app/`), the engineering vault (`docs/`). This is where the product lives. |
| `../thegates-docs/` | **This repo.** The public Sphinx docs site published at `docs.thegates.io`. |
| `../thegates-backend/` | Django + Meilisearch backend serving the API endpoints listed above. |
| `../website/` | Next.js source for `thegates.io/export-plugin` — the export plugin's marketing landing. NOT the main `thegates.io` (which lives elsewhere). `basePath = "/export-plugin"`. |
| `../web-editor/` | Hosts the official Godot Web Editor (Godot's WASM build, not a TheGates-specific editor). Runs on port 8001 locally. A convenience for creators who don't want to install Godot. Not currently mentioned in the docs. |
| `../kinda-safe-godot/` | Historical Linux sandbox experiment. Predates v1.0's cross-platform sandbox. Not load-bearing today. |
| `../thegates-build-containers/` | Build containers for CI. |

### The website voice split

There are **two distinct marketing surfaces**, with deliberately
different voices:

**`thegates.io`** (main marketing — aspirational):
- H1: *"Building a New Internet More Interactive, Social and Fun"*
- Lead: *"We are building a new 3D internet, where instead of scrolling
  Web Pages you can dive into beautiful Digital Worlds"*
- H2 sections: A new Internet, Digital worlds, Unique technology, Free
  and open-source, Encouraging ways to share knowledge..., New
  possibilities, Get involved, Download the app, FAQ.
- CTAs: Download, Build your worlds, Contribute to the project, Join our
  community.
- Vocabulary: *digital worlds*, *3D spaces*, *made by the community*,
  *evolutionary nature*. Capitalizes *"Digital Worlds"* and *"Web Pages"*
  as if they were brand terms. Does not say "metaverse" but addresses it
  in FAQ.

**`thegates.io/export-plugin`** (creator-facing — pragmatic):
- H1: *"Publish your Godot project with just One Click"*
- Tagline: *"Instantly publish your Godot projects. Share with players,
  gather feedback, and deploy updates instantly across Linux, Windows,
  and macOS"*
- Features: One-Click Publishing, Native Performance, Instant Updates,
  Free Hosting.
- Workflow shown: Step 1 *Publish from Godot* → Step 2 *Live on TheGates*.
- CTAs: View in Godot Asset Library, GitHub Repository.

These two voices are **intentional**. The docs match the
export-plugin voice (pragmatic), NOT the main `thegates.io` voice
(aspirational). See [[Voice and audience]] for why.

### How a creator gets from zero to a published gate

1. Install Godot 4.5.
2. Install the TheGates Export plugin from the official Godot Asset
   Library
   ([asset-library/asset/2882](https://godotengine.org/asset-library/asset/2882)).
3. Open the plugin, click *"Publish to TheGates"*.
4. Get a URL back. Share it.
5. (Optional) Self-host instead — any HTTP server works.

This is the canonical happy path. Quickstart already covers it; the
new Introduction should mention it as the primary creator route.

---

## Sources

External:
- [thegates.io](https://thegates.io) — main marketing site.
- [thegates.io/export-plugin](https://thegates.io/export-plugin) —
  export-plugin landing (source in `../website/`).
- [docs.thegates.io](https://docs.thegates.io) — the public docs we're
  working on.
- [Godot Asset Library — TheGates Export](https://godotengine.org/asset-library/asset/2882)
- [Demo video](https://youtu.be/FU4MTPEdqwU)
- [GitHub: thegatesbrowser](https://github.com/thegatesbrowser)
- [Discord](https://discord.com/invite/JwpScU8xm6)
- [lnk.bio/thegates](https://lnk.bio/thegates)

Engineering vault (don't lift prose, only concepts):
- `../thegates/CLAUDE.md` — agent contract for the engine project.
- `../thegates/docs/Index.md` — engineering vault map.
- `../thegates/docs/Architecture Overview.md` — one-page big picture.
- `../thegates/docs/Two-Process Model.md` — launcher + renderer, IPC.
- `../thegates/docs/Gate Format and Lifecycle.md` — the `.gate` spec
  beyond the public reference.
- `../thegates/docs/Launcher App.md` — what's in `app/`.
- `../thegates/docs/Renderer Process.md` — what the sandboxed renderer
  does differently from a normal Godot game.
- `../thegates/docs/Gate Cycle.md` — runtime event sequence.
- `../thegates/docs/Gotchas and Conventions.md` — non-obvious traps.
- `../thegates/godot/notes/Index.md` — engine-fork vault map.
- `../thegates/godot/notes/External Texture Sharing.md` — the shared
  GPU memory mechanism.
- `../thegates/godot/notes/Sandboxing/Index.md` — v1.0 sandbox vault.
- `../thegates/godot/notes/Sandboxing/Architecture.md` — cross-platform
  shape.

Screenshots:
- `../thegates/screenshots/1-home.png` — launcher home (THE visual
  anchor for the Introduction page).
- `../thegates/screenshots/2-loading.png` — gate loading.
- `../thegates/screenshots/3-in-game-ui.png` — inside the Welcome hub.
