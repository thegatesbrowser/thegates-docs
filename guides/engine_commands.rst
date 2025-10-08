.. _doc_engine_commands:

Engine commands
===============

TheGates exposes a small command channel to the running world via the scene tree. Use it to open other gates from within your game and to integrate future features.

Concept
-------

Commands are sent through the root tree with ``send_command`` when available:

.. code-block:: python

   if get_tree().has_method("send_command"):
       get_tree().send_command(command_name, args_array)

API
---

open_gate
~~~~~~~~~

Open another world by URL.

Signature

.. code-block:: python

   get_tree().send_command("open_gate", [url: String])

Parameters

* ``url``: Absolute URL to a ``.gate`` file, e.g. ``https://example.com/my_world.gate``

Behavior

* The current world initiates navigation to the target gate
* Users may experience a short loading step while assets download

Example

.. code-block:: python

   func _on_portal_body_entered(_body: Node) -> void:
       if get_tree().has_method("send_command"):
           get_tree().send_command("open_gate", ["https://your.domain/another_world.gate"])

Notes
-----

* Always guard calls with ``has_method`` to keep worlds runnable outside TheGates.
* Future commands may be added; keep calls feature-detected.

See also
--------

* :ref:`doc_content_hosting`
* :ref:`doc_quickstart`
