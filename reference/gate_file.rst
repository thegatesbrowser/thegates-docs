.. _doc_gate_file:

Gate file
=========

| Worlds are described by a ``.gate`` file. It declares metadata and the
  resources required to load your world.

Concept
-------

| A ``.gate`` file is an INI-like text file with top-level sections and
  ``key = value`` pairs.

Format
------

| Structure:

.. code-block:: ini

   [gate]
   title="Title"
   description="Description"
   icon="path_to/icon.png"
   image="path_to/image.png"
   resource_pack="path_to/pack.zip"
   godot_version="4.5"
   discoverable=true

   [libraries]
   linux.debug.x86_64 = "path_to/yourlib.so"
   linux.release.x86_64 = "path_to/yourlib.so"
   windows.debug.x86_64 = "path_to/yourlib.dll"
   windows.release.x86_64 = "path_to/yourlib.dll"
   macos.debug = "path_to/yourlib.dylib"
   macos.release = "path_to/yourlib.dylib"
   macos.debug.arm64 = "path_to/yourlib.dylib"
   macos.release.arm64 = "path_to/yourlib.dylib"

   # [libraries] section only required if you use GDExtension
   # file paths are relative to the .gate file unless absolute

Fields
------

| ``[gate]``

* ``title``: Display name for the world.
* ``description``: Description shown in gate preview and for indexing in search.
* ``icon``: Path to a small square image used as an icon.
* ``image``: Path to a larger preview/cover image.
* ``resource_pack``: Path to a ZIP containing the exported Godot project.
* ``godot_version``: Target Godot version string (supported versions: ``4.3``, ``4.5``).
* ``discoverable``: ``true`` or ``false``; if ``true``, the world can be indexed.

| ``[libraries]``

* GDExtension libraries to load at runtime. Keys follow the pattern
  ``<os>.<build>[.<arch>]`` and values are file paths.

.. warning::

   | **Windows**, **Linux**, and **macOS** libraries required.
   | **Debug** and **Release** are also required (can be the same file).

Example
-------

| Example ``.gate`` file:

.. code-block:: ini

   [gate]
   
   title="Welcome"
   description="Online Hub for meeting new friends and exploring other worlds"
   icon="exports/welcome_page/image.png"
   image="exports/welcome_page/image.png"
   resource_pack="exports/welcome_page/project.zip"
   godot_version="4.5"
   discoverable=true
   
   [libraries]
   
   linux.debug.x86_64 = "libs/twovoip/v3.10/libtwovoip.linux.template_debug.x86_64.so"
   linux.release.x86_64 = "libs/twovoip/v3.10/libtwovoip.linux.template_release.x86_64.so"
   windows.debug.x86_64 = "libs/twovoip/v3.10/libtwovoip.windows.template_debug.x86_64.dll"
   windows.release.x86_64 = "libs/twovoip/v3.10/libtwovoip.windows.template_release.x86_64.dll"
   macos.debug = "libs/twovoip/v3.10/libtwovoip.macos.template_debug.universal.dylib"
   macos.release = "libs/twovoip/v3.10/libtwovoip.macos.template_release.universal.dylib"
   macos.debug.arm64 = "libs/twovoip/v3.10/libtwovoip.macos.template_debug.universal.dylib"
   macos.release.arm64 = "libs/twovoip/v3.10/libtwovoip.macos.template_release.universal.dylib"
   
   # file paths are relative to the .gate file unless absolute

See also
--------

* :ref:`doc_quickstart`
* :ref:`doc_command_channel`
