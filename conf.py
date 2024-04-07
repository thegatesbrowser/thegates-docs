# Configuration file for the Sphinx documentation builder.

import sphinx
import sphinx_rtd_theme
import sys
import os

# -- Project information

project = 'TheGates'
copyright = '2024-present Nordup'
author = 'Nordup'

release = '(latest)'
version = '0.7.6'

# -- General configuration ------------------------------------------------

needs_sphinx = "1.3"

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "sphinx_tabs.tabs",
    "notfound.extension",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

# Warning when the Sphinx Tabs extension is used with unknown
# builders (like the dummy builder) - as it doesn't cause errors,
# we can ignore this so we still can treat other warnings as errors.
sphinx_tabs_nowarn = True

# Disable collapsing tabs for codeblocks.
sphinx_tabs_disable_tab_closing = True

# Custom 4O4 page HTML template.
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    "title": "Page not found",
    "body": """
        <h1>Page not found</h1>
        <p>
            Sorry, we couldn't find that page. It may have been renamed or removed
            in the version of the documentation you're currently browsing.
        </p>
        <p>
            If you're currently browsing the
            <em>latest</em> version of the documentation, try browsing the
            <a href="/en/stable/"><em>stable</em> version of the documentation</a>.
        </p>
        <p>
            Alternatively, use the
            <a href="#" onclick="$('#rtd-search-form [name=\\'q\\']').focus()">Search docs</a>
            box on the left or <a href="/">go to the homepage</a>.
        </p>
    """,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {'navigation_depth': 2, 'collapse_navigation': False}

# -- Options for OpenGraph

ogp_site_url = "https://thegates.readthedocs.io"
ogp_image = "https://thegates.readthedocs.io/en/latest/_static/social.png"
ogp_description_length = 204
ogp_type = "website"

ogp_custom_meta_tags = [
    '<meta property="og:image:width" content="1200" />',
    '<meta property="og:image:height" content="630" />'
]
