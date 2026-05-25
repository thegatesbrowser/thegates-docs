.. _doc_architecture_overview:

Architecture overview
=====================

| TheGates runs two cooperating processes per gate: a **launcher** (the
  browser UI — the part you see) and a **renderer** (the sandboxed
  world being visited). They run in parallel, share a single GPU
  texture so the world appears seamlessly inside the browser window,
  and talk to each other through a few small inter-process pipes.
|
| This page is the optional read for creators who want to understand
  the model their gate runs inside. If you just want to ship a world,
  :doc:`/getting-started/quickstart` is enough.

.. code-block:: text

   ┌────────────────────────────────────────────┐
   │  Launcher                                  │
   │  ──────────────────────                    │
   │  • Window, input, audio                    │
   │  • Network broker                          │
   │  • File system access                      │
   └────────────────┬───────────────────────────┘
                    │ spawns + restricts
                    ▼
   ┌────────────────────────────────────────────┐
   │  Renderer  (sandboxed, per gate)           │
   │  ──────────────────────                    │
   │  • Loads the gate's .pck                   │
   │  • Renders frames                          │
   │  • No direct network or filesystem         │
   └────────────────────────────────────────────┘

       Shared: a GPU texture (zero-copy frame data),
       plus a few small pipes for input and commands.


Why two processes?
------------------

| Running every visited world in the same process as the browser would
  mean a crash in one world crashes the browser, a hostile world could
  read your browsing history, and every world would have to use the
  same engine version. Splitting them solves all three:
|
| - **Crash isolation.** A renderer crash stops the gate, but the
    browser keeps running.
| - **Sandboxing.** The renderer process is locked down at the OS
    level — see :doc:`/security/overview`.
| - **Per-gate engine versions.** Each gate declares which Godot
    version it needs. The launcher downloads a matching renderer
    binary the first time you visit. A gate built on Godot 4.3 and a
    gate built on Godot 4.5 both run in the same browser.
| - **UI responsiveness.** The browser never blocks waiting for a
    world to load.


The shared texture
------------------

| Each frame, the renderer writes pixels directly into shared GPU
  memory. The launcher displays them in the browser window.
|
| No pixels travel through the inter-process pipes — the only thing
  shared is a GPU memory handle, sent once at startup. This is why
  an embedded world doesn't feel any slower than a standalone Godot
  game.


What the launcher controls
--------------------------

| The launcher process owns the parts of the system gates aren't
  trusted with:
|
| - The desktop window
| - Keyboard and mouse — input events are forwarded to the renderer
    as they happen
| - The network — gates can't open sockets directly, they go through
    a launcher-side broker. See :doc:`/security/network_policy`.
| - The file system — gates only see their own per-gate folder


What the renderer does
----------------------

| The renderer is a minimal Godot runtime stripped of everything not
  needed to draw a world:
|
| - Loads and runs the gate's ``.pck`` file
| - Draws frames into the shared GPU texture
| - Receives input events from the launcher
| - Sends commands back to the launcher (open another gate, request
    mouse capture, and so on)
|
| It cannot open network sockets, read files outside its per-gate
  folder, or draw its own window. The launcher provides what it
  needs.


Why each gate declares its Godot version
----------------------------------------

| The browser keeps a curated set of stable Godot versions (today,
  ``4.3`` and ``4.5``). A gate declares which one it was built
  against in its ``.gate`` manifest, and the browser runs that exact
  version for that gate.
|
| The point is **stability over time**. A gate built today on Godot 4.5
  keeps working when newer gates ship on later versions — the browser
  just spins up the matching renderer for each. The IPC protocol
  between launcher and renderer is stable across versions, so an old
  renderer binary cached on a user's machine still talks to the
  current launcher.
|
| Old renderer binaries live alongside the launcher; new ones get
  downloaded on demand the first time you visit a gate that needs
  them.


See also
--------

- :doc:`/security/overview` — how the OS-level sandbox works on each
  platform.
- :doc:`/security/per_gate_isolation` — why one gate can't see
  another.
- :doc:`/reference/gate_file` — the manifest where ``godot_version``
  is declared.
