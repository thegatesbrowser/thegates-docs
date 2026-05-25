.. _doc_best_practices:

Best practices
==============

| A short list of things worth knowing before you ship a gate. Most of
  these aren't bugs — they're choices you'll make better with the
  context.


Pick your Godot version deliberately
------------------------------------

| The ``godot_version`` field in your ``.gate`` file controls which
  renderer the browser spawns for your gate. Once a gate is in the
  wild, changing the version means the gate is effectively running on
  a different engine — physics, rendering, GDScript parser, all of
  it.
|
| The browser supports a curated set of stable versions (currently
  ``4.3`` and ``4.5``). Pick one and stick with it for the lifetime
  of the gate. If you must switch, test on the new version end-to-end
  first.


``.pck`` vs ``.zip`` — both work
--------------------------------

| The ``resource_pack`` field can point at either format. ``.pck`` is
  Godot's default export and slightly more compact; ``.zip`` is
  easier to inspect and gives you slightly better caching on most
  hosts. Pick whichever fits your workflow.


``discoverable=false`` doesn't mean private
-------------------------------------------

| Setting ``discoverable=false`` keeps your gate out of the
  home-screen search index. It does **not** make the gate private —
  anyone with the URL can still visit. The gate format has no auth
  model.
|
| If you need a private gate, gate access from inside your world's
  logic, or use a hosting setup with HTTP basic auth.


Ship all platforms if you use GDExtension
-----------------------------------------

| If your gate declares any GDExtension library, you need to provide
  a build for **all three platforms** (Windows, Linux, macOS) and
  for **both debug and release**. The library can be a stub if you
  don't actively support a platform — just don't leave it missing.


Update graphics drivers before suspecting code
----------------------------------------------

| On AMD GPUs on Windows, there's a recurring Adrenalin Vulkan
  regression on RDNA1/RDNA2 cards that can produce mesh corruption
  or black-triangle artifacts. Update the GPU driver before assuming
  the bug is in your gate or the engine.


See also
--------

- :doc:`/concepts/what-is-a-gate`
- :doc:`/reference/gate_file`
- :doc:`troubleshooting`
