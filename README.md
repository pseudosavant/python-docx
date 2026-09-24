# ps-python-docx

*ps-python-docx* is John Paul Ellis's fork of [python-docx](https://github.com/python-openxml/python-docx), a Python library for reading, creating, and updating Microsoft Word 2007+ (.docx) files. It is published independently and is not an official upstream release.

This fork starts from upstream 1.2.0. The packaging setup preserves the upstream API and the `docx` import name. Version 1.3.0 adds public theme font and style inheritance APIs. See the [theme API documentation](docs/api/theme.rst). The original MIT license and upstream attribution are preserved.

Version 1.3.1 adds public external hyperlink authoring with `Paragraph.add_hyperlink()`, formatted label runs with `Hyperlink.add_run()`, and read/write tooltip support. See the [text API documentation](docs/api/text.rst).

Version 1.3.2 adds `InlineShape.description` and `InlineShape.title` for reading and writing image alternative text. See the [image metadata documentation](docs/user/shapes.rst).

## Installation

```
pip install ps-python-docx
```

## Example

```python
>>> from docx import Document

>>> document = Document()
>>> document.add_paragraph("It was a dark and stormy night.")
<docx.text.paragraph.Paragraph object at 0x10f19e760>
>>> document.save("dark-and-stormy.docx")

>>> document = Document("dark-and-stormy.docx")
>>> document.paragraphs[0].text
'It was a dark and stormy night.'
```

Install this distribution in place of `python-docx`. Both provide the `docx` package and should not be installed in the same environment.

More information about the inherited API is available in the [upstream documentation](https://python-docx.readthedocs.org/en/latest/). Report fork-specific issues in [this repository](https://github.com/pseudosavant/python-docx/issues).

## Development and releases

Run the unit and acceptance suites without installing the legacy documentation dependencies:

```text
uv sync --locked --no-dev --group test
uv run --locked --no-dev --group test pytest -q
uv run --locked --no-dev --group test behave --format progress --stop --tags=-wip
```

See [RELEASING.md](RELEASING.md) for the GitHub-to-PyPI release process.
