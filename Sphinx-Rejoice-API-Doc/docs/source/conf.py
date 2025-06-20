# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'demosphinxproject'
copyright = '2025, Sayanta Banerjee'
author = 'Sayanta Banerjee'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'rejoice'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "rejoice"
html_logo = '_static/images/rejoice.svg'
html_favicon = '_static/images/rejoice.svg'

html_theme_options = {
    'analytics_anonymize_ip': False,
    'analytics_id': 'G-XXXXXXXXXX',  # Provided by Google in your dashboard
    'autodoc_linebreaks': True,
    'breadcrumb_version': True,
    'description': 'API Documentation',
    'dark_theme': True,
    'dark_theme_caution': False,
    'feedback': True,
    'feedback_url': 'https://feedback.software.keysight.com/form' ,
    'helplink1' : 'Link 1',
    'helplink1_target' : 'https://www.keysight.com/johndoe',
    'insert_version_links_call': 'apiDocsInsertVersionLinks(projectName, currentVersion)',
    'logo_background': 'white',
    'logo_border': '#cdcdcd',
    'page_caching_enabled': True,
    'on_this_page': True,
    'style_external_links': True,
    'support_url': 'https://www.keysight.com/in/en/contact.html' ,
    'version_display': True,
    'version_dropdown': True,
    # Toc options
    'collapse_navigation': True,
    'includehidden': True,
    'navigation_depth': 4,
    'titles_only': True
}