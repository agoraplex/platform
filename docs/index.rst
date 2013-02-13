.. Agoraplex Platform Meta-package documentation master file, created by
   sphinx-quickstart2 on Fri Jan 11 20:37:25 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================
 The `Agoraplex` Platform
==========================

Overview
========

.. include:: narr/blurb.rst

Although designed to function independently, the web application
components work well with the `Pyramid framework
<http://docs.pylonsproject.org/en/latest/docs/pyramid.html>`__

Unless otherwise specified, `Agoraplex` platform components are
licensed under the BSD "3-clause" license. See :doc:`LICENSE` for
details.


Components
==========

The platform consists of:

   - :ref:`anodi <anodi:index>` `:` A decorator-based backport of
     PEP-3107 function annotations to Python 2.7, and related tools.

   - `capsec` `(forthcoming) :` An :wikipedia:`object-capability model`
     toolkit for sharing secure *interprocess* references.

   - :ref:`predicates <predicates:index>` `:` A collection of predicate
     factories, functions, and partials, for functional programming.


.. add non-toc includes in a hidden toc to avoid warnings (borrowed
   from Pyramid docs)

.. toctree::
   :hidden:

   narr/blurb
   LICENSE
