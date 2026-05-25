.. _doc_how_it_works:

How TheGates works
==================

| When you open a gate, TheGates spawns two processes: the **launcher**
  (the browser UI — the part you see) and the **renderer** (the
  sandboxed world being visited). They run in parallel, share a single
  GPU texture so the world appears seamlessly inside the browser window,
  and talk to each other through a few small inter-process pipes.

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
| - **Crash isolation.** A renderer crash stops the gate but the
    browser keeps running.
| - **Sandboxing.** The renderer process is locked down at the OS
    level — see :doc:`/security/overview`.
| - **Per-gate engine versions.** Each gate declares which Godot
    version it needs. The launcher downloads a matching renderer
    binary the first time you visit. A 2026 gate on Godot 4.5 and a
    2030 gate on Godot 5.0 both run in the same browser.
| - **UI responsiveness.** The browser never blocks waiting for a
    world to load.


The shared texture
------------------

| Each frame, the renderer writes pixels directly into shared GPU
  memory. The launcher displays them in the browser window.
|
| No pixels travel through the inter-process pipes — the only thing
  shared is a GPU memory handle, sent once at startup. This is why
  the embedded world doesn't feel any slower than a standalone Godot
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


----

| **Where to go next:**
|
| - :doc:`why-thegates` — the principles behind this architecture.
| - :doc:`/security/overview` — how the sandboxing works on each platform.
| - :doc:`/security/per_gate_isolation` — why gates can't see each other.
