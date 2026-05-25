.. _doc_security_overview:

Sandboxing
==========

| **Browsers sandbox tabs. We sandbox worlds.**

.. note::

   v1.0 ships the foundation of our sandboxing. We'll keep
   strengthening it as the platform grows.

| Every gate you open in TheGates runs in a separate process under an
  OS-level sandbox. Even if a gate's code tries to read your files,
  scan your home network, or talk to your other gates, the operating
  system blocks it.

.. code-block:: text

   Your computer
    ├── Launcher (trusted: your desktop, your network)
    │
    ├── Gate A (locked in its own sandbox)
    │
    └── Gate B (locked in its own sandbox)

    → Gates can't see each other
    → Gates can't read your files
    → Gates can't reach your home network


Built on Chromium
-----------------

| TheGates doesn't roll its own sandbox. Each gate runs in code
  derived from `Chromium's sandbox`_. It's the same isolation Chrome
  uses for browser tabs.
|
| On macOS we also borrow pieces from Firefox's sandbox, which is
  itself derived from Chromium.

.. _Chromium's sandbox: https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/design/sandbox.md


Three platforms, one sandbox
----------------------------

.. tabs::

   .. tab:: Windows

      | Each gate runs inside a Windows **AppContainer**: an isolated
        security context with a restricted access token and the
        lowest possible integrity level.
      |
      | The gate can read and write its per-gate folder and the
        gate's project file, and nothing else under your user
        profile. It cannot create network sockets.

   .. tab:: Linux

      | Each gate runs with three layers stacked on top of each other:
      |
      | - **Landlock** restricts what the gate can read or write on
          disk to its per-gate folder and the GPU device.
      | - **Capability dropping** strips all root-like permissions.
      | - **seccomp** filters the syscalls the gate can make.
          Network-creating syscalls aren't allowed.

   .. tab:: macOS

      | Each gate runs under **Seatbelt**, Apple's kernel-enforced
        sandbox. The profile is deny-by-default: the gate gets
        read/write on its per-gate folder, access to the GPU, and
        audio output if you've granted it.
      |
      | Everything else is blocked at the kernel.


What gates can't reach
----------------------

| Gates can't talk to your home router, your printer, or services
  running on your own machine. The launcher process owns all network
  connections. Before opening a socket for a gate, the broker checks
  the destination. Public addresses on the open internet are allowed.
  Private IP ranges and loopback are denied.

.. seealso::

   :doc:`/security/network_policy` for details on what's allowed and
   what's blocked.


Trust gates like websites
-------------------------

| The sandbox is a **hardening layer, not a guarantee**. Treat gates
  the same way you treat websites: explore freely, and use the same
  judgment you'd use online.
|
| The sandbox raises the bar against hostile code in a gate so a
  single bad gate doesn't compromise your machine. It doesn't
  replace your own sense of what's worth opening.


Found a bug?
------------

| If you find a way to break out of the sandbox with a gate that
  doesn't involve a kernel bug, that's worth a report.
|
| Email **nordup.ondr@gmail.com** with a reproducer. Subject line
  ``[TheGates security]`` so it doesn't get lost.


See also
--------

- :doc:`/security/per_gate_isolation`
- :doc:`/security/network_policy`
- :doc:`/security/wayland_and_x11`
- :doc:`/about/faq`
