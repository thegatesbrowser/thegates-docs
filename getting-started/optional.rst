.. _doc_optional:

Native libraries (GDExtension)
==============================

| If your gate uses Godot's GDExtension to load native libraries, you
  need to declare them in your ``.gate`` file. The export plugin
  doesn't auto-detect these yet — you'll need to edit the manifest
  manually.

* Copy the GDExtension file section **[libraries]** to the gate file.

* Edit paths to match their relative URL paths.

.. code-block:: toml

   # your_project.gate
   [gate]
   title="GDExtension project"
   description="This should work"
   icon="path_to/icon.png"
   image="path_to/image.png"
   resource_pack="path_to/pack.zip"
   godot_version="4.5"

   [libraries]
   linux.debug.x86_64 = "path_to/yourlib.so"
   linux.release.x86_64 = "path_to/yourlib.so"
   windows.debug.x86_64 = "path_to/yourlib.dll"
   windows.release.x86_64 = "path_to/yourlib.dll"
   macos.debug = "path_to/yourlib.dylib"
   macos.release = "path_to/yourlib.dylib"
   macos.debug.arm64 = "path_to/yourlib.dylib"
   macos.release.arm64 = "path_to/yourlib.dylib"

   # file paths are relative to the .gate file unless absolute

.. warning::

   | **Windows**, **Linux**, and **macOS** libraries required.
   | **Debug** and **Release** are also required (can be the same file).

| See more in :doc:`/reference/gate_file`.


See also
--------

* :doc:`/getting-started/hosting`
* :doc:`/getting-started/linking-gates`
* :doc:`/reference/gate_file`
