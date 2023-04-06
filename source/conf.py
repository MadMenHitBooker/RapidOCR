import os
import sys

sys.path.insert(0, os.path.abspath('../'))

from get_pypi_latest_version import GetPyPiLatestVersion


project = 'RapidOCR'
copyright = 'RapidAI'
author = 'RapidAI'

latest_version = GetPyPiLatestVersion()('rapidocr_onnxruntime')
release = f'v{latest_version}'
repo_url = 'https://github.com/RapidAI/RapidOCR'

extensions = [
    'myst_parser',
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
]

autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': True,
    'undoc-members': True,
    'exclude-members': '__weakref__, __dict__,__module__',
    'private-members': True
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_logo = "./_static/RapidOCR_LOGO.png"
html_static_path = ['_static']
html_js_files = [
    'redefined_logo_url.js',
]
