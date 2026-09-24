Theme fonts
===========

The document theme contains major (heading) and minor (body) font families.
Changing these fonts affects text that references the corresponding theme slots.
It does not apply direct formatting to runs or rewrite style definitions.

.. code-block:: python

    document.theme_fonts.name = "Company fonts"
    document.theme_fonts.major_latin = "Aptos Display"
    document.theme_fonts.minor_latin = "Aptos"

These properties control Latin fonts. East Asian, complex-script, supplemental
fonts, theme colors, and effects are preserved. Optional metrics associated with
the old Latin typeface are removed when that typeface is assigned.

Access creates a complete default theme if the document has none. An existing
malformed or incomplete font scheme raises ``ValueError``.

``ThemeFonts`` objects
----------------------

.. autoclass:: docx.theme.ThemeFonts
   :members:
