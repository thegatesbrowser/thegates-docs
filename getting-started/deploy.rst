.. _doc_deploy:

Deploying your world
====================

Serve your ``.gate``, pack ``.zip/.pck``, and images over HTTPS with correct MIME types and CORS.

Essentials
----------

* Files must be accessible by direct URL (no auth needed)
* Recommend HTTPS and ``Cache-Control`` headers for static assets
* Ensure correct content types: ``.gate`` as ``text/plain`` or ``application/toml``; ``.pck/.zip`` as ``application/octet-stream``; images as standard types

Local server (Python)
---------------------

.. code-block:: bash

   python3 -m http.server 8000
   # Open: http://localhost:8000/your_project.gate

Node.js (http-server)
---------------------

.. code-block:: bash

   npm install -g http-server
   http-server . -p 8000 --cors

Nginx
-----

.. code-block:: nginx

   server {
       listen 80;
       server_name your.domain;
       root /var/www/your_world;

       location / {
           try_files $uri =404;
       }

       types {
           text/plain gate;
           application/toml toml;
           application/octet-stream pck zip;
       }

       add_header Access-Control-Allow-Origin "*";
       add_header Cache-Control "public, max-age=31536000";
   }

GitHub Pages
------------

1. Push your static files to a repository (``/docs`` or ``gh-pages`` branch)
2. Enable Pages in repo settings
3. Visit ``https://<user>.github.io/<repo>/your_project.gate``

Cloudflare Pages
----------------

1. Create a new project from your repo
2. Set build command to ``-`` (static) and output dir to the folder with your files
3. Verify your gate URL loads publicly over HTTPS

Netlify
-------

1. Drag-and-drop your static folder or connect repo
2. Add headers in ``_headers`` if needed:

.. code-block:: text

   /*
     Access-Control-Allow-Origin: *
   
   *.pck
     Content-Type: application/octet-stream
     Cache-Control: public, max-age=31536000

Troubleshooting
---------------

* 404: Check file paths and case sensitivity
* CORS: Add ``Access-Control-Allow-Origin: *`` headers
* Wrong content type: Set explicit types for ``.gate`` and ``.pck/.zip``
* Mixed content: Use HTTPS for all assets

Next steps
----------

* See :ref:`doc_quickstart` and :ref:`doc_content_hosting`
* Link to other worlds: see :ref:`doc_command_channel`
