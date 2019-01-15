DRF tutorial
============

DRF tutorial

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

To start the application just build and run the docker local.yml image:

::
   
   $ docker-compose -f local.yml build
   $ docker-compose -f local.yml up


Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the tests:

::

    $ docker-compose -f local.yml run --rm django pytest --reuse-db
