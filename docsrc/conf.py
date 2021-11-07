# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime
from pathlib import Path
from typing import Dict, Optional, Tuple

import toml  # type: ignore

# -- Project information -----------------------------------------------------

project_root = Path()
if Path().resolve().name == "docsrc":
    project_root = project_root.resolve().parent
print(project_root.resolve())
pyproject = toml.loads((project_root / "pyproject.toml").read_text())
project = pyproject["tool"]["poetry"]["name"]
author = ", ".join(pyproject["tool"]["poetry"]["authors"])
year = datetime.date.today().year
project_copyright = f"{year}, {author}"
release = pyproject["tool"]["poetry"]["version"]
version = release


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    # "sphinx_autodoc_typehints",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    # "sphinxcontrib.spelling",
    # TODO: enable spelling
]

autodoc_typehints = "description"

intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]] = {
    "python": ("https://docs.python.org/3", None),
}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language: Optional[str] = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

python_use_unqualified_type_names = True
add_module_names = False
autodoc_type_aliases = {
    "ReplacementPolicy": "ReplacementPolicy",
    "Entry": "Entry",
    "bitmath.Bitmath": "bitmath.Bitmath",
    "Pickler": "Pickler",
    "RWLock": "RWLock",
    "FuncParams": "FuncParams",
    "FuncReturn": "FuncReturn",
    "PathLike": "PathLike",
}

smartquotes = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# autodoc_member_order = "bysource
autodoc_default_options = {
    "member-order": "bysource",
    "undoc-members": True,
    "show-inheritance": False,
}
