About
============

Add-on that allows displaying Blogging based blogs inside a Collage.

Installing
============

This package requires Plone 3.x or later (tested on 3.3.x and 4.0a2).

Installing without buildout
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install this package in either your system path packages or in the lib/python
directory of your Zope instance. You can do this using either easy_install or
via the setup.py script.

Installing with buildout
~~~~~~~~~~~~~~~~~~~~~~~~

If you are using `buildout`_ to manage your instance installing
collective.blogging is even simpler. You can install
collective.blogging by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.blogging

After updating the configuration you need to run the ''bin/buildout'', which
will take care of updating your system.

.. _buildout: http://pypi.python.org/pypi/zc.buildout


Copyright and Credits
=====================

collective.collage.blogging is licensed under the GPL. See LICENSE.txt for details.

Author: `Davi Lima`__

.. _davi-lima: mailto:davilima6@gmail.com

__ davi-lima_

Contributors:

- `Lukas Zdych`__

.. _lzdych: mailto:lukas.zdych@gmail.com

__ lzdych_


Homepage: collective.collage.blogging_.

.. _collective.collage.blogging: http://plone.org/products/collective.collage.blogging

