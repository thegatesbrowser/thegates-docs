.. _doc_intro:

Introduction
============

| Inspired by `Ready Player One`_ and the concept of 3D Internet.
  We wanted to create a space where many different worlds would be connected into one universe.
  And those worlds can be made and hosted by everyone 🌌

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

It’s very similar to the Internet \(World Wide Web\):

#. You search or type a link of the world you wanna visit.
#. TheGates browser downloads all the necessary files and opens them.
#. Inside this world, you can find other links/portals and follow them.
 
| While the Web is built of HTML and JavaScript.
  We have **Godot Engine** that provides similar functionality.

Why does Godot Engine work like HTML and JavaScript?
----------------------------------------------------

Godot uses scenes to describe objects and GDScript to make them behave, so:

.. code-block:: ini

   Scenes (saved to tscn file) ~ html files.
   GDScript ~ javascript.

| And the magic here is that Godot can export project files in .pck or .zip format.
| Then it can load the exported file and run it right away ✨


Read more
---------

* :doc:`/security/overview`
* :doc:`/about/faq`
* :doc:`/community/contribute`
