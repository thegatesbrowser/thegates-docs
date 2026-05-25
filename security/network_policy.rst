.. _doc_security_network_policy:

Network policy
==============

| Gates can't scan your home network. The launcher owns every network
  connection. A gate doesn't open sockets directly, it asks the
  launcher's broker, and the broker decides whether the destination
  is allowed.


What's allowed
--------------

| Public addresses on the open internet. A gate can talk to its own
  backend, fetch assets from CDNs, connect to multiplayer servers
  hosted online, and so on. This is the normal case. Most gates
  need network access to function.


What's blocked
--------------

| Anything that points back into your own machine or your local
  network:
|
| - **Your computer.** Loopback addresses (``127.0.0.1``, ``::1``).
    A gate can't reach a development server, a database, or any
    other service running on the same machine.
| - **Your home network.** Private IPv4 ranges (``10.0.0.0/8``,
    ``172.16.0.0/12``, ``192.168.0.0/16``) and the IPv6 equivalents.
    A gate can't probe your router, your printer, or other devices
    on your LAN.
| - **Link-local addresses.** ``169.254.0.0/16`` and ``fe80::/10``.
    Often used by WSL, Docker, and zero-config services.
| - **Carrier-grade NAT.** ``100.64.0.0/10``. Used by Tailscale and
    some VPNs.
| - **Multicast.** ``224.0.0.0/4`` and IPv6 multicast. Blocks
    network-discovery attacks.

.. note::

   The broker enforces this on the launcher side, *before* a socket
   is opened. The gate never gets a chance to connect to a blocked
   destination, because there's no socket for it to use.


Why this matters
----------------

| Without the broker, a malicious gate could:
|
| - Map your home network and identify services on it.
| - Attack your router's admin interface (which usually trusts
    requests from the local network).
| - Reach development tools running on your machine that don't expect
    hostile input.
|
| With the broker, none of this is reachable. The gate sees the open
  internet only.


See also
--------

- :doc:`/security/overview`
- :doc:`/security/per_gate_isolation`
