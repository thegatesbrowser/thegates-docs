TheGates Docs
=============

| **A web browser for 3D worlds.**
| Visit Godot-built worlds via URL. No installs, no accounts, sandboxed by default.

----

Choose your path
----------------

Explore worlds
~~~~~~~~~~~~~~

| Download TheGates from `thegates.io <https://thegates.io>`__, paste any
  gate URL into the address bar, and walk in.

* :doc:`What is TheGates? </about/introduction>`
* :doc:`Frequently asked questions </about/faq>`

Build a gate
~~~~~~~~~~~~

| If you know `Godot Engine <https://godotengine.org>`__, you can publish a
  gate in five minutes.

* :doc:`Quickstart </getting-started/quickstart>` — your first gate, end-to-end
* :doc:`How it works </concepts/how-it-works>` — the two-process model in plain language
* :doc:`Why TheGates? </concepts/why-thegates>` — the worldview behind it

Contribute to the engine
~~~~~~~~~~~~~~~~~~~~~~~~

| TheGates is open source. Help shape the 3D internet.

* :doc:`How to contribute </community/contribute>`
* `Source code on GitHub <https://github.com/thegatesbrowser>`__

----

What's new in v1.0
------------------

| Cross-platform sandboxing — every gate runs locked down on Windows,
  Linux, and macOS. :doc:`Read the sandboxing overview </security/overview>`.

----

Get involved
------------

| If you don't understand something or cannot find what you are looking for,
  help us improve the documentation by letting us know. Fix mistakes, add examples, or suggest edits, every contribution helps.
|
| Submit an issue or pull request on the `GitHub repository <https://github.com/thegatesbrowser/thegates-docs>`__
  or talk to us on the `Discord server <https://discord.com/invite/JwpScU8xm6>`__.

Links
-----

* Website: `thegates.io <https://thegates.io>`__
* GitHub: `thegatesbrowser <https://github.com/thegatesbrowser>`__
* Demo video: `YouTube <https://youtu.be/FU4MTPEdqwU?si=dNm3yFojDD1Ga08m>`__

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: About
   :name: sec-general

   about/introduction.rst
   about/faq.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Concepts
   :name: sec-concepts

   concepts/why-thegates.rst
   concepts/how-it-works.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Get started
   :name: sec-getting-started

   getting-started/quickstart.rst
   getting-started/hosting.rst
   getting-started/optional.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Security
   :name: sec-security

   security/overview.rst
   security/per_gate_isolation.rst
   security/network_policy.rst
   security/wayland_and_x11.rst
   security/verify_the_sandbox.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Reference
   :name: sec-reference

   reference/gate_file.rst
   reference/command_channel.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Community
   :name: sec-community

   community/contribute.rst
   community/community.rst
