.. _doc_why_thegates:

Why TheGates?
=============

| Most "3D internet" platforms ask you to install a client, create an
  account, and live inside their walled garden. TheGates is the
  opposite — a browser. You paste a URL, the world loads, and the
  rest is yours.
|
| Five ideas hold the whole thing up.


Gates are URLs
--------------

| Worlds are addressable like webpages. Paste a URL, the gate opens.
  Share a URL, the gate spreads.
|
| There's no central app store, no review queue, no platform to
  publish through. The web works this way for a reason — open at the
  edges, open by default.


Each gate runs in its own sandbox
---------------------------------

| Every world you open runs in a separate process under OS-level
  isolation, built on Chromium's sandbox code. Your filesystem, your
  home network, and your other gates are off-limits to a gate's code.
|
| Even if a gate is hostile, the operating system blocks it.
  See :doc:`/security/overview`.


Built on Godot Engine
---------------------

| TheGates renders worlds with `Godot Engine`_, an open-source 3D
  engine. If you can build with Godot, you can build a gate — scenes
  are your HTML, GDScript is your JavaScript.
|
| No proprietary editor. No platform lock-in. No "we'll ban your
  account for terms violations" — your gate lives on your server, or
  any server.

.. _Godot Engine: https://godotengine.org


Two processes, not one
----------------------

| The browser and the world are separate processes. A crash in one
  doesn't kill the other. Each gate declares which Godot version it
  needs, and the browser supports a curated set of stable versions —
  so a gate built on Godot 4.3 keeps working even after newer gates
  ship on later versions.
|
| See :doc:`how-it-works` for the architecture in plain language.


Self-host anywhere
------------------

| A gate is a small bundle of static files. Any HTTP server can host
  one — your own VPS, Cloudflare Pages, Netlify, an S3 bucket, a
  Raspberry Pi at home.
|
| There's no platform to publish through, no fees, no review process.
  See :doc:`/getting-started/hosting`.


----

| **Where to go next:**
|
| - :doc:`how-it-works` — the technical architecture behind these principles.
| - :doc:`/getting-started/quickstart` — ship your first gate in five minutes.
| - :doc:`/security/overview` — how the sandboxing works on each platform.
