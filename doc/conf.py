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
    'sphinx.ext.intersphinx',
    'numpydoc',
    'nbsphinx',
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = False

numpydoc_class_members_toctree = False

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']
source_suffix = '.rst'
# The encoding of source files.
source_encoding = 'utf-8-sig'
master_doc = 'index'

# General information about the project
year = datetime.date.today().year
project = u'GMT/Python'
copyright = u'2017-2018, Leonardo Uieda and Paul Wessel'
if len(__version__.split('+')) > 1 or __version__ == 'unknown':
    version = 'dev'
else:
    version = __version__

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
html_extra_path = ['.nojekyll', 'CNAME']
pygments_style = 'default'
add_function_parentheses = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

# Theme config
html_theme = "sphinx_rtd_theme"
html_theme_options = {
}
html_context = {
    'menu_links': [
        ('<i class="fa fa-play fa-fw"></i> Try it online!', 'http://try.gmtpython.xyz'),
        ('<i class="fa fa-github fa-fw"></i> Source Code', 'https://github.com/GenericMappingTools/gmt-python'),
        ('<i class="fa fa-users fa-fw"></i> Contributing', 'https://github.com/GenericMappingTools/gmt-python/blob/master/CONTRIBUTING.md'),
        ('<i class="fa fa-book fa-fw"></i> Code of Conduct', 'https://github.com/GenericMappingTools/gmt-python/blob/master/CODE_OF_CONDUCT.md'),
        ('<i class="fa fa-gavel fa-fw"></i> License', 'https://github.com/GenericMappingTools/gmt-python/blob/master/LICENSE.txt'),
        ('<i class="fa fa-comment fa-fw"></i> Contact', 'https://gitter.im/GenericMappingTools/gmt-python'),
    ],
    # Custom variables to enable "Improve this page"" and "Download notebook"
    # links
    'doc_path': 'doc',
    'github_repo': 'GenericMappingTools/gmt-python',
    'github_version': 'master',
}

# intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
}

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
