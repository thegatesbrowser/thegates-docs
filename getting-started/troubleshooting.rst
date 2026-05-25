.. _doc_troubleshooting:

Troubleshooting
===============

| Things that commonly go wrong and what to try. If your issue isn't
  listed here, ask on
  `Discord <https://discord.com/invite/JwpScU8xm6>`__ — most weekdays
  you'll get a reply within an hour.


Export plugin doesn't appear in Godot
-------------------------------------

| **Symptom:** You installed the TheGates Export plugin but it doesn't
  show up in your project.
|
| **Try:** Enable the plugin in *Project → Project Settings → Plugins*.
  The plugin needs to be enabled per-project, not just installed once
  globally.


Gate URL doesn't open in TheGates
---------------------------------

| **Symptom:** You paste a URL into the launcher and nothing happens,
  or it shows an error.
|
| **Try:**
|
| - Check the URL points directly at a ``.gate`` file, not at a
    project's home page.
| - Open the URL in any web browser — if it doesn't load, the gate
    isn't reachable. Your hosting may be down or the path is wrong.
| - If the URL works in a browser but not in TheGates, the ``.gate``
    manifest may be malformed. See :doc:`/reference/gate_file` for
    the expected format.


Gate opens but the world is blank or black
------------------------------------------

| **Symptom:** The launcher shows the gate's UI overlay but the 3D
  world doesn't appear.
|
| **Try:**
|
| - Check the ``resource_pack`` path in the ``.gate`` file is
    reachable. Paths are relative to the ``.gate`` URL.
| - On AMD GPUs on Windows, update your graphics driver. There's a
    known Vulkan regression on certain Adrenalin versions that
    breaks mesh rendering.
| - Check the launcher's debug log (``F12`` in the launcher) for
    errors from the renderer process.


GDExtension libraries don't load
--------------------------------

| **Symptom:** Your gate uses GDExtension but the native code doesn't
  work when published.
|
| **Try:**
|
| - Check the ``[libraries]`` section in your ``.gate`` declares
    builds for **all three platforms** (Windows, Linux, macOS) and
    **both debug and release**. Missing entries fail silently.
| - Library paths in the ``.gate`` are relative to the ``.gate`` URL.
    Make sure they resolve.
| - See :doc:`optional` for the exact format.


Gate works locally but not when published
-----------------------------------------

| **Symptom:** Everything works when you serve the gate from a local
  HTTP server, but breaks once published.
|
| **Try:**
|
| - Check that all asset URLs in your ``.gate`` are relative paths,
    not absolute paths to ``localhost``.
| - Confirm your hosting serves the files correctly — most static
    hosts handle this automatically.
| - Open the gate URL directly in a web browser to confirm everything
    is reachable.


Renderer feels slow or laggy
----------------------------

| **Symptom:** Your gate runs at low FPS or stutters.
|
| **Try:**
|
| - The first visit to a gate downloads the renderer binary if the
    user doesn't have it cached — that's a one-time cost. Repeat
    visits should be fast.
| - Check your world's render settings — *Forward+* at very high
    settings can be heavier than necessary for simpler scenes.
| - Open the launcher's debug log (``F12``) and look at the boot-time
    logs to see where time is being spent.


See also
--------

- :doc:`/community/community` — get help from the community.
- :doc:`best-practices` — avoid common pitfalls before they happen.
