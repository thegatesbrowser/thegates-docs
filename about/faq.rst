.. _doc_faq:

Frequently asked questions
==========================

| Short answers to the most common questions about TheGates.
| Follow the links for deeper documentation.


For visitors
------------

Is this a metaverse?
~~~~~~~~~~~~~~~~~~~~

| Not exactly.
|
| TheGates treats the internet as a network of 3D worlds you open
  by URL — closer to the web browser model than to a single
  centralized platform.


Do I install worlds separately?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| No.
|
| Opening a gate works more like opening a website than installing
  a game. The launcher downloads the gate automatically when you
  visit its URL.


Where can I find worlds to visit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The launcher home screen includes featured gates and a search bar.
|
| One of the featured gates is **Welcome** — a 3D hub world with
  portals to other gates.
|
| You can also paste a direct gate URL from a friend or website.


Which platforms does TheGates support?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Windows, Linux, and macOS.
|
| Download the launcher from
  `thegates.io <https://thegates.io>`__.


For creators
------------

What do I need to build a gate?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| - `Godot 4.5 <https://godotengine.org/download/>`__
| - Rendering method set to ``Forward+``
| - A ``.gate`` manifest referencing your exported project
|
| See :doc:`/getting-started/quickstart`.


How do I publish a gate?
~~~~~~~~~~~~~~~~~~~~~~~~

| Install the
  `TheGates Export plugin <https://godotengine.org/asset-library/asset/2882>`__
  from the Godot Asset Library, click
  **Publish to TheGates**, and you get a hosted URL back.
|
| Self-hosting on your own HTTP server is also supported.
|
| See :doc:`/getting-started/hosting`.


Can I self-host my gate?
~~~~~~~~~~~~~~~~~~~~~~~~

| Yes.
|
| A gate is just a manifest and exported files served over HTTP.
  Any normal HTTP server works.
|
| See :doc:`/getting-started/hosting`.


Can gates link to other gates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Yes.
|
| Gates can open other gates by URL, similar to webpages linking
  to other webpages.
|
| See :doc:`/getting-started/linking-gates`.


Can I use GDExtension or native libraries?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Yes.
|
| Add platform-specific libraries in the ``[libraries]`` section
  of your ``.gate`` file.
|
| See :doc:`/reference/gate_file`.


Does every gate run its own engine version?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Yes.
|
| Each gate declares the Godot version it was built against.
  The launcher downloads and runs the matching renderer version
  for that gate.
|
| This allows older gates to keep working even as newer renderer
  versions ship.
|
| See :doc:`/architecture/overview`.


Trust and safety
----------------

Is it safe to run third-party worlds?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Every gate runs in its own OS-level sandbox on Windows,
  Linux, and macOS.
|
| A gate cannot directly access your files, your home network,
  or other running gates.
|
| Treat gates the same way you treat websites: trusted to the
  extent you trust the publisher.
|
| See :doc:`/security/overview`.


Is TheGates open source?
~~~~~~~~~~~~~~~~~~~~~~~~

| Yes.
|
| The launcher, renderer, backend, and tooling are open source.
|
| Explore the repositories on
  `GitHub <https://github.com/thegatesbrowser>`__.


Need more help?
---------------

| Join the community or open an issue on GitHub.

* :doc:`/community/community`
* :doc:`/community/contribute`
