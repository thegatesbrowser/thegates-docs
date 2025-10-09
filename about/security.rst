.. _doc_content_security:

Security model
==============

| All modern browsers come with the feature called `sandboxing`_.
| It's when the proccess running untrusted code is isolated from the operating system
  and cannot cause any harm or steal any data.
| 
| Our sandboxing implementation is currently under development in this branch:
| `https://github.com/thegatesbrowser/godot/tree/chromium-sandboxing <https://github.com/thegatesbrowser/godot/tree/chromium-sandboxing>`__
| 
| Meanwhile, all new projects hosted are monitored and checked for security.

.. _sandboxing: https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/design/sandbox.md

.. note::

   If you are familiar with C++ and wanna help, please contact us.
   We would appreciate any help. Links are in the :ref:`community page <doc_content_community>`.