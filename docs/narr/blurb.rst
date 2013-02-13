The `Agoraplex` platform is a collection of tools for building
applications in Python based on a healthy mix of idiomatic Python and
sexy paradigms, including:

    - :wikipedia:`Representational State Transfer`

      Yes, we `HATEOAS <http://en.wikipedia.org/wiki/HATEOAS>`__, too.

    - :wikipedia:`Functional programming`

      ...especially :wikipedia:`Function composition (computer science)`


Core philosophies embodied in the platform (i.e., our `favorite
Kool-Aid flavors
<http://en.wikipedia.org/wiki/Drinking_the_Kool-Aid>`__):

    - `Small pieces, loosely joined <http://www.smallpieces.com/>`__.

      ...both in Weinberger's original sense, and in the sense that we
      try to maximize cohesion within the platform's parts, and make
      each part maximally useful on its own. Specifically, we strive
      to make each piece of the platform as focused as we can, keeping
      dependencies "down" the stack, not "across" it.

      E.g., most of the platform depends on :ref:`anodi
      <anodi:index>`, because it provides a fundamental *language*
      service (function annotations).

      Few things depend on `capsec`, though, because its focus is on
      the very narrow problem of manipulating secure interprocess
      references. While a component might depend on interprocess
      references, it might *not* require them to be secure. If it
      requires them to be secure, it might *not* require that security
      to be capabilities-based. Thus, `capsec`, though *applicable*,
      is not *required*. Less code, fewer imports, fewer files, less
      pollution, world peace. Modest goals.

    - `Strong opinions
      <http://www.saffo.com/02008/07/26/strong-opinions-weakly-held/>`__,
      `weakly held
      <http://bobsutton.typepad.com/my_weblog/2006/07/strong_opinions.html>`__

      The platform is opinionated, inasmuch as the *path of least
      resistance* reflects our opinions and best practices, as refined
      over time. However, the platform also does its best *not* to
      stand in the way of your forming your own opinions, and revising
      them as you "prove yourself wrong."
