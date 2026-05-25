.. _doc_intro:

Introduction
============

| TheGates is a web browser for 3D worlds. Instead of webpages, you
  visit Godot-built spaces where people meet, play, build, and hang out.
|
| The idea is a 3D Internet — many worlds connected into one universe,
  made and hosted by everyone. (Yes, like `Ready Player One`_, if you
  want a touchstone.) 🌌

.. _Ready Player One: https://en.wikipedia.org/wiki/Ready_Player_One_(film)


What is TheGates?
-----------------

| **TheGates** is a new web ecosystem focused on building communities, exploring worlds and gaming with friends.
  Instead of webpages it consists of 3D experiences build with `Godot Engine <https://godotengine.org/>`__.

Safe by design
--------------

| Every gate runs in an OS-level sandbox. Your filesystem, your home network, and your other gates are
  isolated from anything a gate's code might do. See :doc:`/security/overview`.

3D Internet
-----------

| We wanted the internet to be more in line with how we as humans interact with each other and the world around us.
  And to do so, it has to operate in 3D space with physics.
| 
| Basically, the Internet is a virtual environment where people and organizations interact with each other and exchange information.
  And if so, the question is: why do we restrict ourselves to 2D pages and hyperlinks for all these activities?


Why it matters
--------------

| After we’ve built the initial prototype, I found out that meeting people in the 3D space and connecting with them,
  not just through text, but being able to interact with them is a really valuable human experience.

Vision
------

| We envision a future where 3D spaces replace static social media — places where people can hang out, create,
  and connect through games, music, art, and live shows. Personal worlds will become creative hubs, and learning
  will become more immersive and efficient through interactive 3D experiences. This shift will spark a new
  ecosystem of internet projects and fuel the next wave of innovation.

How does it work?
-----------------

It's very similar to how you browse the Web:

#. You search for or paste a link to the world you want to visit.
#. TheGates downloads the necessary files and opens the world.
#. Inside, you find more links and portals that take you to other worlds.

| The Web is built on HTML and JavaScript. TheGates is built on
  **Godot Engine** — scenes are your HTML, GDScript is your JavaScript.

.. code-block:: ini

   Scenes (saved to .tscn)  ~  html files
   GDScript                 ~  javascript

| Godot can export a whole project to a single ``.pck`` or ``.zip``
  file. The browser downloads that file and runs it directly ✨


Read more
---------

* :doc:`/security/overview`
* :doc:`/about/faq`
* :doc:`/community/contribute`
