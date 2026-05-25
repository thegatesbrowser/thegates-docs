.. _doc_security_wayland_and_x11:

Wayland and X11
===============

| On Linux, TheGates picks Wayland automatically when your session
  supports it. Wayland gives gates stronger isolation than X11 —
  if you're on a Wayland session, you don't need to do anything to
  benefit from it.


Why Wayland is preferred
------------------------

| Wayland was designed from the ground up around per-client
  isolation. Each application gets its own surface, its own
  clipboard, and its own input — applications can't peek at each
  other's windows or grab each other's keystrokes.
|
| X11 doesn't provide that isolation by default. Hardening gates
  further on X11 is ongoing work for us. The sandbox still protects
  your filesystem, network, and process boundaries, but window and
  clipboard isolation between gates and your other applications is
  weaker than on Wayland.


How we handle both
------------------

| - **On Wayland**: each gate gets a per-client Wayland surface. The
    compositor enforces isolation between gates and between gates
    and your other applications.
| - **On X11 (including XWayland)**: TheGates shows a one-time
    warning explaining the reduced isolation. The sandbox still
    protects your filesystem, network, and process boundaries — but
    clipboard and screen-capture isolation is up to X11, not us.


Use Wayland if you can
----------------------

| If your distribution supports a Wayland session for your desktop
  environment, use it. Most major desktops have shipped Wayland
  sessions by default for years (GNOME since 2017, KDE Plasma 6,
  Sway, Hyprland, and others).
|
| If you must run X11, treat gates with extra caution — same as you
  would any untrusted application sharing your X11 session.


See also
--------

- :doc:`/security/overview`
- :doc:`/security/per_gate_isolation`
