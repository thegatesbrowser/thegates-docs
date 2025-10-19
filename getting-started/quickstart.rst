.. _doc_quickstart:

Quickstart
==========

| Follow this guide to publish your first project to TheGates.

Prerequisites
-------------

* Install `Godot Engine 4.5 <https://godotengine.org/download/>`__.
* In your project, set the rendering method to ``Forward+``.

Start from the template (optional)
----------------------------------

| Already have a Godot 4.5 project? Open it in Godot 4.5 and skip this section.
  If you're starting from scratch, use the official multiplayer starter project with VOIP:

* GitHub: `thegatesbrowser/godot-multiplayer <https://github.com/thegatesbrowser/godot-multiplayer>`__

| Clone and open in Godot 4.5:

.. code-block:: bash

   git clone https://github.com/thegatesbrowser/godot-multiplayer.git
   cd godot-multiplayer

| The template includes:

* Third‑person controller with client interpolation
* Ready‑to‑use client/server multiplayer
* 3D positional voice chat (VOIP) and basic UI

Exporting
---------

| Then you need to create some files. Download and check out the `demo project`_ as an example.
| 
| 1. Export your project as a pack file **(zip preferred)**. See Godot documentation on `exporting packs`_.

.. image:: img/export_pck.png
   :height: 350

| 2. Create an icon and a thumbnail image.
| 
| 3. Create gate file as shown below.

.. code-block:: toml

   # your_project.gate
   [gate]

   title="Your project name"
   description="This will be in search"
   icon="path_to/icon.png"
   image="path_to/image.png"
   resource_pack="path_to/pack.zip"
   godot_version="4.5"

   # file paths are relative to the .gate file unless absolute

| After doing this, you will have 4 files: **project pack**, **icon**, **thumbnail image**, **gate file**.

.. note:: 

   | You can use `TheGates Export Plugin`_ that creates everything for you.

.. _demo project: https://drive.google.com/file/d/1Vhf-NlfKl3oCEglXQRu3TP1yOdlPUMrF/view
.. _exporting packs: https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html
.. _TheGates Export Plugin: https://godotengine.org/asset-library/asset/2882

Test locally
------------

* Start a simple HTTP server in the folder with your ``.gate`` file.

.. code-block:: bash

   python3 -m http.server 8000

* In `TheGates app`_, open: ``http://localhost:8000/your_project.gate``.

| Alternatively, you can use `Servez`_.

.. _Servez: https://greggman.github.io/servez/
.. _TheGates app: https://thegates.io/

Next steps
----------

* :doc:`/getting-started/hosting` in your server.
* Follow :doc:`/getting-started/optional`.
* Join the :doc:`/community/community` for help and feedback.
