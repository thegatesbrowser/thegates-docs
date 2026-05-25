.. _doc_security_verify:

Verifying the sandbox is engaged
================================

| The sandbox engages automatically for every gate. There's no
  setup or permission prompt. If a gate's lockdown fails, the
  renderer aborts rather than running unprotected (we call this
  fail-closed).
|
| TheGates doesn't yet show a visible "sandbox: on" indicator per
  gate. If you want to confirm engagement for a specific gate, the
  launcher writes detailed logs you can inspect.


Open the log
------------

| 1. Inside the launcher, press **F12** to open the **Debug Log**
    window.
| 2. Near the bottom, find the line ``Logs written to ...`` and
    click the path to open the log file in your default editor.
|
| The log captures everything from the gate's startup, including
  the sandbox engagement. The sandbox markers are hard to miss.
  Look for the "lockdown engaged" line and the ``SANDBOX-DIAG``
  block near the top of the file.


Engineering verification
------------------------

| The TheGates engineering team runs an autotest harness that
  exercises every sandbox engagement path on every supported
  platform, including negative tests that force each sandbox step
  to fail and confirm the renderer aborts. The harness lives in the
  `engine repository <https://github.com/thegatesbrowser/godot>`__.
|
| If you find a way to launch a gate where the sandbox isn't
  engaged, or a way to break out of an engaged sandbox without a
  kernel bug, that's worth a security report. Email
  **nordup.ondr@gmail.com** with a reproducer. Subject line
  ``[TheGates security]`` so it doesn't get lost.


See also
--------

- :doc:`/security/overview`
- :doc:`/community/contribute`
