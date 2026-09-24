# Publishing ps-python-docx

This fork publishes the `ps-python-docx` distribution from `pseudosavant/python-docx`. Its import package remains `docx`. Keep the original upstream attribution and MIT license.

The version comes from `src/docx/__init__.py`. Fork versions describe this distribution. They do not represent releases approved by the upstream project. Version 1.3.0 adds public theme font and style inheritance APIs to the upstream 1.2.0 baseline.

## One-time configuration

Enable GitHub Actions and create a GitHub environment named `pypi`. The PyPI pending publisher must specify:

| Setting | Value |
| --- | --- |
| Project | `ps-python-docx` |
| Owner | `pseudosavant` |
| Repository | `python-docx` |
| Workflow filename | `publish.yml` |
| Environment | `pypi` |

The publishing job requests an OIDC token with `id-token: write`. Do not add a PyPI API token secret. Creating the environment or merging the workflows does not publish a package.

## Release procedure

1. Merge the intended changes and update the fork changelog.
2. Set `docx.__version__` to the chosen release version and run `uv lock`.
3. Merge the release preparation changes after CI passes.
4. Create a GitHub release from that commit with a tag exactly matching `v` plus the package version, for example `v1.3.0`.
5. Publish the GitHub release to start `.github/workflows/publish.yml`.

The release workflow reuses CI to run the unit and acceptance suites, check the tag and package identity, build the wheel and source distribution, validate metadata, and test the installed wheel. Only after those checks pass does the publishing job download those exact artifacts and upload them to PyPI.

The first successful upload creates the PyPI project through the pending publisher. A draft GitHub release does not start publishing. Do not use an existing upstream tag for a fork release unless it points to the intended fork commit with the correct metadata and workflows.

## Local package checks

```text
uv sync --locked --no-dev --group test --group release
uv run --locked --no-dev --group test --group release pytest -q
uv run --locked --no-dev --group test --group release behave --format progress --stop --tags=-wip
uv run --locked --no-dev --group release python scripts/check_release.py
uv build --no-sources
uv run --locked --no-dev --group release twine check dist/*
```

The dedicated groups avoid installing the upstream project's old documentation toolchain just to test or release the fork.

## Preparing upstream contributions

The `codex/theme-font-api` branch starts at the upstream-compatible `master` base
and contains only the theme API, style inheritance support, documentation, and
tests. It does not rename the distribution or change the upstream version.

The publishing branch carries those feature commits separately from fork
packaging and the 1.3.0 version change. Submit the feature branch upstream when
ready. Keep upstream fixes on that branch first, then cherry-pick them onto the
publishing branch. Avoid submitting fork branding, release workflows, version
numbers, or Markdown-specific policy with the library API.
