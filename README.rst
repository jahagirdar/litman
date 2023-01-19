======
LitMan
======


.. image:: https://img.shields.io/pypi/v/litman.svg
        :target: https://pypi.python.org/pypi/litman

.. image:: https://img.shields.io/travis/jahagirdar/litman.svg
        :target: https://travis-ci.com/jahagirdar/litman

.. image:: https://readthedocs.org/projects/litman/badge/?version=latest
        :target: https://litman.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A mindmap based knowledgebase for PDF files.


* Free software: BSD license
* Documentation: https://litman.readthedocs.io.

This package is inspired by [Docear](https://docear.org/).

I find Docear's extraction of Highlights and comments from PDF documents, and creating a mindmap from it, very useful.

Regretfully Docear has a few drawbacks.

* It has a clunks interface.
* It has certain requirements from the pdf viewer. Most of the pdf viewers available in linux do not meet these requirements.
* Its development has stopped. The last release was in 2015.

This is my attempt at making a docear like tool that I can use in my day to day work.


Features
--------

* Parse a mindmap
* Extract list of pdf documents under the `litman` node
* Search documents for comments and highlights.
* Create/Update childnodes with the highlight.
* Save updated mindmap



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
