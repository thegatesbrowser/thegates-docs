.. _doc_linking_gates:

Linking to other gates
======================

| One of the most powerful patterns in TheGates is portals between
  gates. From inside a world, you can ask the browser to navigate to
  another gate URL. It's the equivalent of an ``<a href>`` link on
  a webpage, but triggered from GDScript.


The basic call
--------------

| From any script in your gate:

.. code-block:: gdscript

   if get_tree().has_method("send_command"):
       get_tree().send_command("open_gate", ["https://example.com/world.gate"])

| The ``has_method`` guard makes your gate forward-compatible. If
  the browser ever changes the command channel API, older gates still
  work without crashing.
|
| The browser navigates the user to the target gate. The current
  gate's renderer is torn down. Same flow as if the user pasted the
  URL into the address bar.


Relative URLs work too
----------------------

| If the target gate is hosted at the same URL prefix as yours, you
  can pass a relative path:

.. code-block:: gdscript

   get_tree().send_command("open_gate", ["sequel.gate"])

| The browser resolves this against the current gate's URL. Useful
  for series of connected gates hosted under one path.


Opening external URLs
---------------------

| To open a non-gate URL (a YouTube video, a Discord invite, a
  marketplace listing) in the user's system browser, use
  ``open_link`` instead:

.. code-block:: gdscript

   get_tree().send_command("open_link", ["https://thegates.io"])

| The browser hands the URL to the OS. The current gate keeps
  running.


Portal UX tips
--------------

| - **Make portals visible.** Players should see a portal coming from
    a distance and understand it leads somewhere new.
| - **Confirm before navigating.** A misclicked portal that whisks
    the player away mid-game is frustrating. Consider a "Press F to
    enter" prompt.
| - **Indicate the destination.** Show the title or preview of the
    target gate before transition, the same way a hyperlink shows
    its URL on hover.


See also
--------

- :doc:`/reference/command_channel`
- :doc:`/reference/gate_file`
