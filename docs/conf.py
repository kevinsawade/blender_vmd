"""Sphinx configuration."""
project = "Blender VMD"
author = "Kevin Sawade"
copyright = "2023, Kevin Sawade"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
