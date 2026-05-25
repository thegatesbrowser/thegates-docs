.. _doc_hosting:

Hosting your projects
=====================

| Skip this page if "Publish to TheGates" in the :doc:`quickstart` is
  enough — your project is already hosted. The rest is for people who
  want to serve the files themselves.


Export your project
-------------------

In the plugin: ``Advanced settings`` → ``Export locally`` → ``Export to
local folder``.

.. image:: img/export_plugin_local.png
   :width: 400

You get a folder containing:

- a ``.gate`` manifest
- a ``.pck`` or ``.zip`` resource pack
- icon and preview images
- optionally, GDExtension libraries

.. note::

   Paths inside the ``.gate`` file are relative to its own URL. Upload
   the whole folder under one URL prefix so the relative paths
   resolve.


Serve the folder
----------------

Anything that serves static files over HTTP or HTTPS works: your own
server (Nginx, Caddy, Apache), a static host (Cloudflare Pages,
Netlify, Vercel, GitHub Pages), or object storage with a public bucket
(S3, R2, B2).

The launcher is a desktop app, not a web browser — there are no CORS
requirements, no special headers, and no MIME-type configuration. It
uses standard HTTP caching (``ETag`` / ``If-Modified-Since``), so any
sensible host handles re-downloads efficiently.


Open in TheGates
----------------

The URL of the ``.gate`` file is the gate URL. Paste it into the TheGates app:

.. code-block:: text

  https://your-host.example.com/yourproject.gate

| See :doc:`/getting-started/optional` for linking between gates.
