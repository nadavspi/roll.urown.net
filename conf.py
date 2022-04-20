#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# roll.urown.net documentation build configuration file, created by
# sphinx-quickstart on Tue Apr 29 19:40:41 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
#sys.path.append(os.path.abspath('sphinxcontrib-srclinks'))
sys.path.insert(0, os.path.abspath('_ext'))
import sphinx_rtd_theme
#import solar_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx_last_updated_by_git',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Roll Your Own Network'
author = 'Alain Wolf & contributors'
copyright = '2014, 2022 Alain Wolf & contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '3'
# The full version, including alpha/beta/rc tags.
#release = '3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

highlight_language = 'bash'
linenothreshold = 5

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
#pygments_style = 'monokai'
pygments_style = 'solarizeddark'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

todo_include_todos = True

git_last_updated_timezone = 'Europe/Zurich'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# For the Spinx RTD theme see
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html_theme
# and /usr/local/lib/python2.7/dist-packages/sphinx_rtd_theme/theme.conf
html_theme_options = {
  #'canonical_url': 'https://roll.urown.net/',
  'prev_next_buttons_location' : 'both',
  'style_external_links': True,
  'vcs_pageview_mode': 'edit',
};

html_context = {
  'display_github': True,
  'github_user': 'alainwolf',
  'github_repo': 'roll.urown.net',
  'github_version': 'master/',
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_theme_path = [solar_theme.theme_path]

# The base URL which points to the root of the HTML documentation. It is used
# to indicate the location of document using The Canonical Link Relation.
# Default: ''.
html_baseurl = 'https://roll.urown.net/'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['_html_extra']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'https://roll.urown.net/'

# Language to be used for generating the HTML full-text search index. This
# defaults to the global language selected with language. If there is no support
# for this language, "en" is used which selects the English language.
# Support is present for these languages:
#     da – Danish
#     nl – Dutch
#     en – English
#     fi – Finnish
#     fr – French
#     de – German
#     hu – Hungarian
#     it – Italian
#     ja – Japanese
#     no – Norwegian
#     pt – Portuguese
#     ro – Romanian
#     ru – Russian
#     es – Spanish
#     sv – Swedish
#     tr – Turkish
#     zh – Chinese
html_search_language = 'en'

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'roll.urown.net'

# srclink settings
#srclink_project = 'https://github.com/alainwolf/roll.urown.net'
#srclink_src_path = ''
#srclink_branch = 'master'

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     '**': [
#         'localtoc.html',
#         'relations.html',
#         'searchbox.html',
#         'srclinks.html',
#         ],
#     'index': [
#         'globaltoc.html',
#         'relations.html',
#         'searchbox.html',
#         'srclinks.html',
#         ],
# }

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'roll.urown.net.tex', 'Roll Your Own Network',
   'roll.urown.net', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'roll.urown.net', 'Roll Your Own Network',
     ['roll.urown.net'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'roll.urown.net', 'Roll Your Own Network',
   'roll.urown.net', 'roll.urown.net', 'How to Roll Your Own Network Services.',
   'Privacy'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'roll.urown.net'
epub_author = 'roll.urown.net'
epub_publisher = 'roll.urown.net'
epub_copyright = '2014, 2021, roll.urown.net'

# The basename for the epub file. It defaults to the project name.
#epub_basename = 'roll.urown.net'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = 'en'

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# A string of reStructuredText that will be included at the end of every source
# file that is read.
rst_epilog = """

.. |publicDomain|     replace:: example.net
.. |privateDomain|    replace:: lan

.. |publicIPv4|       replace:: 198.51.100.240

.. |IPv4Subnet|       replace:: 192.0.2.0/24
.. |IPv6Subnet|       replace:: |IPv6Prefix|/64
.. |IPv6Prefix|       replace:: 2001:db8:c0de\:\:

.. |SIPserverIPv4|    replace:: 192.0.2.27
.. |SIPserverIPv6|    replace:: 2001:db8::27

.. |CAsiteIPv4|         replace:: 192.0.2.28
.. |CAsiteIPv6|         replace:: 2001:db8:face::28

.. |ownCloudIP4|      replace:: 192.0.2.29
.. |ownCloudIP6|      replace:: 2001:db8:face::29

.. |HTTPserverIPv4|   replace:: 192.0.2.30

.. |BOOKserverIPv4|   replace:: 192.0.2.33
.. |BOOKserverIPv6|   replace:: 2001:db8:1::33


.. |OPDSserverIPv4|   replace:: 192.0.2.34
.. |OPDSserverIPv6|   replace:: 2001:db8::34

.. |BitTorrentServerIPv4|   replace:: 192.0.2.36
.. |BitTorrentServerIPv6|   replace:: 2001:db8:1::36

.. |XMPPIPv4|         replace:: 192.0.2.35
.. |XMPPIPv6|         replace:: 2001:db8:face::35

.. |KeyServerIPv4|    replace:: 192.0.2.37
.. |KeyServerIPv6|    replace:: 2001:db8::37

.. |BitcoinIPv4|      replace:: 192.0.2.39
.. |BitcoinIPv6|      replace:: 2001:db8::39

.. |mailserverIPv4|   replace:: 192.0.2.40
.. |mailserverIPv6|   replace:: 2001:db8::40

.. |DNSMasterIPv6|    replace:: 2001:db8:2::41

.. |DNSSlaveAIPv4|    replace:: 198.51.100.41
.. |DNSSlaveAIPv6|    replace:: 2001:db8:f00d::41
.. |DNSSlaveBIPv4|    replace:: 203.0.113.41
.. |DNSSlaveBIPv6|    replace:: 2001:db8:idea::41
.. |DNSSlaveCIPv4|    replace:: 198.18.249.0.41
.. |DNSSlaveCIPv6|    replace:: 2001:db8:face::41

.. |DnsResolverAIPv4|  replace:: 192.0.2.43
.. |DnsResolverAIPv6|  replace:: 2001:db8::43

.. |TorClientIPv4|    replace:: 192.0.2.48
.. |TorClientIPv6|    replace:: 2001:db8::48
.. |TorServerIPv4|    replace:: 192.0.2.49
.. |TorServerIPv6|    replace:: 2001:db8::49

.. |DnsResolverBIPv4|  replace:: 192.0.2.51
.. |DnsResolverBIPv6|  replace:: 2001:db8::51

.. |IMAP| replace::    :abbr:`IMAP (Internet Message Access Protocol)`
.. |LDA| replace::     :abbr:`LDA (Local Delivery Agent)`
.. |LMTP| replace::    :abbr:`LMTP (Local Mail Delivery Protocol)`
.. |MDA| replace::     :abbr:`LDA (Mail Delivery Agent)`
.. |MSA| replace::     :abbr:`MSA (Mail Submission Agent)`
.. |MTA| replace::     :abbr:`MTA (Message Transfer Agent)`
.. |MUA| replace::     :abbr:`MUA (Mail User Agent)`
.. |SMTP| replace::    :abbr:`SMTP (Simple Mail Transport Protocol)`
.. |TLS| replace::     :abbr:`TLS (Transport Layer Security)`
.. |XMPP| replace::    :abbr:`XMPP (Extensible Messageing and Presence Protocol)`
.. |software-center| image:: /scbutton-free-200px.*
.. |software-center2| image:: /software-center-icon-48.*

"""
