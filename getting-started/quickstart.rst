.. _doc_quickstart:

Quickstart
==========

This page is a short overview with links to the full guides.

Prerequisites
-------------

* Install `Godot Engine 4.5 <https://godotengine.org/download/>`__.
* In your project, set the rendering method to ``Forward+``.
* For a complete step‑by‑step, see :ref:`doc_content_hosting`.

Start from the template (recommended)
-------------------------------------

Use the official multiplayer starter project with VOIP:

* GitHub: `thegatesbrowser/godot-multiplayer <https://github.com/thegatesbrowser/godot-multiplayer>`__

Clone and open in Godot 4.5:

.. code-block:: bash

   git clone https://github.com/thegatesbrowser/godot-multiplayer.git
   cd godot-multiplayer

The template includes:

* Third‑person controller with client interpolation
* Ready‑to‑use client/server multiplayer
* 3D positional voice chat (VOIP) and basic UI

Create your gate (summary)
--------------------------

1. Export your project as a pack file (``.zip`` preferred). See `exporting packs <https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html>`__.
2. Create a thumbnail image (``.png``, 16:9 preferred).
3. Create a ``.gate`` file next to your assets, for example:

.. code-block:: toml

   # your_project.gate
   [gate]
   title = "Your project name"
   description = "This will be in search"
   icon = ""
   image = "path/image.png"
   resource_pack = "path/pack.zip"
   godot_version = "4.5"

   # 'path' is relative to this file, or an absolute URL

Test locally
------------

* Start a simple HTTP server in the folder with your ``.gate`` file.

.. code-block:: bash

   python3 -m http.server 8000

* In TheGates app, open: ``http://localhost:8000/your_project.gate``.

Open in TheGates
----------------

* Download the app: `thegates.io <https://thegates.io/>`__.
* Paste the URL to your ``.gate`` file and browse your world.

Link to other worlds
--------------------

From GDScript, you can open another gate URL:

.. code-block:: python

   if get_tree().has_method("send_command"):
       get_tree().send_command("open_gate", ["https://example.com/project.gate"])

GDExtension (optional)
----------------------

To load native libraries, add a ``[libraries]`` section to your gate file and provide platform builds. See :ref:`doc_content_hosting` for details and requirements.

Next steps
----------

* Read :ref:`doc_content_hosting` for the full workflow.
* Deploy to the web: :ref:`doc_deploy`.
* Use engine commands: :ref:`doc_command_channel`.
* Learn the model: :ref:`doc_content_intro`.
* Join the :ref:`doc_content_community` for help and feedback.


