.. _doc_command_channel:

Command channel
===============

| TheGates exposes a small command channel to the parent process via the scene tree.
  Use it to open other gates or external links from within your world.

Concept
-------

| Commands are sent through the root tree with ``send_command``:

.. code-block:: python

   if get_tree().has_method("send_command"):
       get_tree().send_command(command_name, args_array)

API
---

open_gate
~~~~~~~~~

| Open another world by URL.
| 
| Signature

.. code-block:: python

   get_tree().send_command("open_gate", [url: String])

| Parameters

* ``url``: Absolute URL to a ``.gate`` file, e.g. ``https://example.com/world.gate``

| Behavior

* Closes the active world and transitions to the requested gate.

| Example

.. code-block:: python

   func on_portal_entered(_body: Node) -> void:
       if get_tree().has_method("send_command"):
           get_tree().send_command("open_gate", ["https://example.com/world.gate"])

open_link
~~~~~~~~~

| Open an external link.
| 
| Signature

.. code-block:: python

   get_tree().send_command("open_link", [link: String])

| Parameters

* ``link``: Absolute URL to open, e.g. ``https://example.com``

| Behavior

* Opens the link in the default web browser.

| Example

.. code-block:: python

   func on_click_link() -> void:
       if get_tree().has_method("send_command"):
           get_tree().send_command("open_link", ["https://example.com"])

Notes
-----

* Guard calls with ``has_method`` to keep worlds runnable outside TheGates.
* Future commands may be added; ask us on Discord if you need something.

See also
--------

* :ref:`doc_quickstart`
* :ref:`doc_content_community`
