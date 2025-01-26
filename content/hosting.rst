.. _doc_content_hosting:

Hosting your projects
=====================

To host your project, first you need to make sure it's compatable with `Godot Engine 4.3`_.

.. _Godot Engine 4.2: https://godotengine.org/download/archive/

Exporting
---------

| Then you need to create some files. Download and check out `demo project`_ as example.
| 
| 1. Export your project as pack file **\(zip preffered\)**. See godot documantation on `exporting packs`_.

.. image:: img/export_pck.png
   :height: 350

| 2. Create thumbnail image **\(png, 16:9 preffered\)**.
| 
| 3. Create gate file as shown below.

.. code-block:: ini

   # your_project.gate
   [gate]

   title="Your project name"
   description="This will be in search"
   image="path/image.png"
   resource_pack="path/pack.zip"

   # 'path' relative to your gate file
   # or absolute url

| After doing this you will have 3 files: **project pack**, **thumbnail image**, **gate file**.

.. note:: 

   | You can use `TheGates Export Plugin`_ that creates everything for you.

.. _demo project: https://drive.google.com/file/d/1Vhf-NlfKl3oCEglXQRu3TP1yOdlPUMrF/view
.. _exporting packs: https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html
.. _TheGates Export Plugin: https://godotengine.org/asset-library/asset/2882

Hosting on a server
-------------------

| Now you are ready to host your project and open it in TheGates.
| 
| To test it locally use `python SimpleHttpServer`_ or `Servez`_.
| 
| Just start your server, type gate file url in `TheGates app`_ and voilà.
| Example: ``http://localhost:8000/your_project.gate``

.. _python SimpleHttpServer: https://www.hackerearth.com/practice/notes/simple-http-server-in-python/
.. _Servez: https://greggman.github.io/servez/
.. _TheGates app: https://nordup.itch.io/the-gates

.. note:: 

   | If you have any difficulties ask the :ref:`community <doc_content_community>`.
   | To host on our server email us on thegates.browser@gmail.com
   | 
   | * Further steps are optional and not required.

Linking
-------

To make a user to follow a link to another gate call from GDScript:

.. code-block:: python

   if get_tree().has_method("send_command"):
      get_tree().send_command("open_gate", ["https://example.com/project.gate"])

GDExtension
-----------

To load gdextension shared libraries:

* Copy gdextension file section **\[libraries\]** to gate file.

* Edit paths to much their relative url paths.

.. code-block:: ini

   # your_project.gate
   [gate]
   title="GDExtension project"
   description="This should work"
   image="path/image.png"
   resource_pack="path/pack.zip"

   [libraries]
   linux.debug.x86_64 = "path/your.so"
   linux.release.x86_64 = "path/your.so"
   windows.debug.x86_64 = "path/your.dll"
   windows.release.x86_64 = "path/your.dll"
   macos.debug = "path/your.dylib"
   macos.release = "path/your.dylib"
   macos.debug.arm64 = "path/your.dylib"
   macos.release.arm64 = "path/your.dylib"

   # 'path' relative to your gate file
   # or absolute url

.. warning:: 

   | **Windows**, **Linux** and **MacOS** libraries required.
   | **Debug** and **Release** also required \(can be the same file\).
