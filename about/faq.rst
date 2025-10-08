.. _doc_faq:

FAQ
===

Is this a new metaverse?
------------------------

Not exactly. TheGates treats the internet as a network of 3D worlds (built with Godot) that you can browse via links, similar to how you navigate web pages today.

What do I need to build a world?
--------------------------------

* `Godot 4.5 <https://godotengine.org/download/>`__
* Rendering method set to ``Forward+``
* A ``.gate`` file that references your exported pack and images (see :ref:`doc_quickstart`)

How do I host and test locally?
-------------------------------

Run a local HTTP server in your project folder and open your ``.gate`` URL in TheGates app. See :ref:`doc_content_hosting`.

Which platforms does TheGates support?
--------------------------------------

Windows, Linux, and macOS.

Where do I download the app?
----------------------------

From `thegates.io <https://thegates.io/>`__.

Is it open-source?
------------------

Yes, the project is open-source. Explore the repositories on `GitHub <https://github.com/thegatesbrowser>`__.

Is it safe to run third-party worlds?
-------------------------------------

Sandboxing is under active development (see :ref:`doc_content_security`). In the meantime, new hosted projects are monitored and reviewed.

Can I link to other worlds from my game?
----------------------------------------

Yes. Use the engine command from GDScript (see example in :ref:`doc_content_hosting`).

Can I use GDExtension/native libraries?
---------------------------------------

Yes. Provide platform builds in the ``[libraries]`` section of your ``.gate`` file. See :ref:`doc_content_hosting` for the exact format and requirements.

Where can I get help?
---------------------

Join our :ref:`doc_content_community` (Discord, social, email), or open an issue on GitHub.


