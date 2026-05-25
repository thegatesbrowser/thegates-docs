.. _doc_security_per_gate_isolation:

Per-gate isolation
==================

| Each gate you open in TheGates is isolated from every other gate.
  A hostile gate cannot read another gate's saved data, peek at its
  network traffic, or talk to its renderer process.


Gates can't see each other
--------------------------

| If you open a phishing gate and a banking-themed gate in the same
  session, the phishing gate has no way to reach into the banking
  gate's local storage. They live in separate sandboxes, with
  separate identities at the operating system level.
|
| Each gate gets:
|
| - **Its own per-gate folder** — saved data is namespaced under the
    gate's URL. One gate's folder is invisible to another gate.
| - **Its own sandbox identity** — a separate AppContainer profile on
    Windows, a separate Seatbelt profile on macOS, a separate
    Landlock ruleset on Linux.
| - **Its own IPC channels** — the inter-process channels between
    each gate and the launcher are per-gate. A gate cannot connect
    to another gate's channels.


What's not isolated
-------------------

| The launcher process is shared — it routes your input, manages the
  desktop window, and brokers all network traffic. The launcher is
  the trusted side of the boundary; everything inside a gate is
  treated as untrusted.
|
| Your TheGates settings, bookmarks, and history live in the
  launcher's own data directory, which gates cannot read or write.


See also
--------

- :doc:`/security/overview`
- :doc:`/security/network_policy`
