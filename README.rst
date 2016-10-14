===============================
proxyguy
===============================


.. image:: https://img.shields.io/pypi/v/proxyguy.svg
        :target: https://pypi.python.org/pypi/proxyguy

.. image:: https://img.shields.io/travis/yudori/proxyguy.svg
        :target: https://travis-ci.org/yudori/proxyguy

.. image:: https://readthedocs.org/projects/proxyguy/badge/?version=latest
        :target: https://proxyguy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/yudori/proxyguy/shield.svg
     :target: https://pyup.io/repos/github/yudori/proxyguy/
     :alt: Updates


proxyguy helps you manage and switch between different network proxy environments and configurations (or none at all) in your linux computer


* Free software: MIT license
* Documentation: https://proxyguy.readthedocs.io.


Installation
--------

Download/Clone this project to your local system. In the proxyguy directory, run

``pip install .``

NOTE: requires that pip has already been installed you the system.


Usage
--------

To view available commands, simply run: 

``proxyguy``


Use the following to create a new proxy configuration:

``proxyguy new``

then fill in required fields.


To activate, run:

``proxyguy activate <profile_name>``

where <profile_name> is the name of a created configuration profile



Features
--------

* Create and activate different proxy configuration environments


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

