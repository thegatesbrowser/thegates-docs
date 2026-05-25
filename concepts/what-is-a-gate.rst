.. _doc_what_is_a_gate:

What is a gate?
===============

| A gate is the unit of content in TheGates — analogous to a webpage,
  but instead of HTML it points at an exported Godot project and the
  runtime needed to play it.


The shape of a gate
-------------------

| Any gate hosted on the web is made of **three URLs**:
|
| 1. **The .gate manifest** — a small INI file (the gate's address card)
| 2. **The resource pack** — a ``.pck`` or ``.zip`` containing the
    exported Godot project
| 3. **The icon and preview image** — used on the launcher's home
    screen and in gate descriptions
|
| Plus implicitly: the **renderer binary** for the Godot version
  declared in the manifest. The browser downloads and caches it the
  first time it's needed.


The manifest
------------

| The ``.gate`` file is the address card. It declares the title, the
  resource pack, the preview image, and which Godot version this gate
  was built against:

.. code-block:: ini

   [gate]
   title = "My World"
   description = "..."
   icon = "icon.png"
   image = "preview.png"
   resource_pack = "world.zip"
   godot_version = "4.5"
   discoverable = true

| See the :doc:`/reference/gate_file` reference for the full field
  list.


What happens when you visit a gate
----------------------------------

| 1. You paste or click a gate URL.
| 2. The browser downloads the ``.gate`` manifest.
| 3. The browser downloads the resource pack and assets (or uses its
    cache).
| 4. The browser finds or downloads the matching renderer binary.
| 5. The browser spawns the renderer, hands it the pack, and shows
    the first frame.
|
| All of this takes a few seconds for a cached gate, or about as long
  as a webpage takes to load for a fresh one.


Why each gate declares its Godot version
----------------------------------------

| The browser keeps a curated set of stable Godot versions. A gate
  declares which one it was built against, and the browser runs that
  exact version for that gate.
|
| The point is **stability over time**. A gate built today on Godot
  4.5 keeps working when newer gates ship on later versions — the
  browser just spins up the matching renderer for each.


See also
--------

- :doc:`how-it-works` — the architecture behind this.
- :doc:`/reference/gate_file` — the full manifest spec.
