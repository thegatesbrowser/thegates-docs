.. _doc_optional:

Optional steps
==============

Link to other worlds
--------------------

| To make a user follow a link to another gate, call from GDScript:

.. code-block:: python

   if get_tree().has_method("send_command"):
      get_tree().send_command("open_gate", ["https://example.com/project.gate"])

| See more in :doc:`/reference/command_channel`.

GDExtension
-----------

| To load GDExtension shared libraries:

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


Next steps
----------

* :doc:`/getting-started/hosting` in your server.
* Check out :doc:`/reference/command_channel`.
* Join the :doc:`/community/community` for help and feedback.
