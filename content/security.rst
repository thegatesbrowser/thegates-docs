.. _doc_content_security:

Security Model
==============

| All modern browsers come with the feature called **sandboxing**.
| It's when the proccess running untrusted code is isolated from the operating system
  and cannot cause any harm or steal any data.

Our sandboxing implementation is under development. Current status will be displayed below:

* **Linux** sandboxing is implemented but it's not tested fully, so be careful.
* **Windows** version doesn't have sandboxing - meaning it's not secure to open non trusted gates.

.. note::

   If you are good at C++ and wanna help, please contact us.
   We would appreciate any help. Links are in the :ref:`community page <doc_content_community>`.