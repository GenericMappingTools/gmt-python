# -*- coding: utf-8 -*-
import sys
import os
import datetime
import sphinx_rtd_theme

# Sphinx needs to be able to import the package to use autodoc and get the
# version number
sys.path.append(os.path.pardir)

from gmt import __version__, __commit__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'numpydoc',
    'nbsphinx',
]

# Produce pages for each class and function
autosummary_generate = True
autodoc_default_flags = ['members', 'inherited-members']

numpydoc_class_members_toctree = False

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build', '.ipynb_checkpoints']
source_suffix = '.rst'
# The encoding of source files.
source_encoding = 'utf-8-sig'
master_doc = 'index'

# General information about the project
year = datetime.date.today().year
project = u'GMT/Python'
copyright = u'2017, Leonardo Uieda'
version = 'dev ({})'.format(__commit__[:7])

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(year=year)

html_last_updated_fmt = '%b %d, %Y'
html_title = 'GMT/Python'
html_short_title = 'GMT/Python'
html_logo = '_static/gmt-python-logo.png'
html_favicon = '_static/favicon.png'
html_static_path = ['_static']
html_extra_path = ['.nojekyll']
pygments_style = 'default'
add_function_parentheses = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# Theme config
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
}
html_context = {
    'menu_links': [
        ('Contributing', 'https://github.com/GenericMappingTools/gmt-python/blob/master/CONTRIBUTING.md'),
        ('Code of Conduct', 'https://github.com/GenericMappingTools/gmt-python/blob/master/CODE_OF_CONDUCT.md'),
        ('Contact', 'https://gitter.im/GenericMappingTools/gmt-python'),
        ('<i class="fa fa-github"></i> Source Code', 'https://github.com/GenericMappingTools/gmt-python'),
    ],
}

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
