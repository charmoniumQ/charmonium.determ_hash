==========================
charmonium.determ_hash
==========================

.. image:: https://img.shields.io/pypi/v/charmonium.determ_hash
   :alt: PyPI Package
   :target: https://pypi.org/project/charmonium.determ_hash
.. image:: https://img.shields.io/pypi/dm/charmonium.determ_hash
   :alt: PyPI Downloads
   :target: https://pypi.org/project/charmonium.determ_hash
.. image:: https://img.shields.io/pypi/l/charmonium.determ_hash
   :alt: PyPI License
.. image:: https://img.shields.io/pypi/pyversions/charmonium.determ_hash
   :alt: Python Versions
.. image:: https://img.shields.io/github/stars/charmoniumQ/charmonium.determ_hash?style=social
   :alt: GitHub stars
   :target: https://github.com/charmoniumQ/charmonium.determ_hash.git
.. image:: https://github.com/charmoniumQ/charmonium.determ_hash.git/actions/workflows/main.yaml/badge.svg
   :alt: CI status
   :target: https://github.com/charmoniumQ/charmonium.determ_hash.git/actions/workflows/main.yaml
.. image:: https://img.shields.io/github/last-commit/charmoniumQ/charmonium.determ_hash
   :alt: GitHub last commit
   :target: https://github.com/charmoniumQ/charmonium.determ_hash.git/commits
.. image:: https://img.shields.io/librariesio/sourcerank/pypi/charmonium.determ_hash
   :alt: libraries.io sourcerank
   :target: https://libraries.io/pypi/charmonium.determ_hash
.. image:: https://img.shields.io/badge/docs-yes-success
   :alt: Documentation link
.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: https://mypy.readthedocs.io/en/stable/
   :alt: Checked with Mypy
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

A deterministic hash for arbitray objects

Python's default |hash|_ will give different results each process invocation, in order to thwart
denial-of-service attacks based on intentionally triggering hash collisions (see ``-R`` in `Python's
CLI options`_). Even setting ``PYTHONHASHSEED`` is not enough, because the hash can still use
non-deterministic data such as pointer-addresses. By default, this package uses the `xxhash`_
algorithm, which is the fastest non-cryptographic hash I know of.

Quickstart
----------

If you don't have ``pip`` installed, see the `pip install
guide`_.

.. _`pip install guide`: https://pip.pypa.io/en/latest/installing/

.. code-block:: console

    $ pip install charmonium.determ_hash

>>> from charmonium.determ_hash import determ_hash
>>> determ_hash(b"hello world")
141361478936837800319111455324245712876

.. |hash| replace:: ``hash``
.. _`hash`: https://docs.python.org/3/library/functions.html?highlight=hash#hash
.. _`Python's CLI options`: https://docs.python.org/3/using/cmdline.html
.. _`xxhash`: https://cyan4973.github.io/xxHash/
