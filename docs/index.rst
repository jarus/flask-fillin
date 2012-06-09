============
Flask-fillin
============

.. currentmodule:: flask.ext.fillin

This Flask extension provides simple utilities for **testing your forms** in 
Flask application.

Installation
============
The installation is thanks to the Python Package Index and `pip`_ really simple.

.. code-block:: console

   $ pip install Flask-fillin

If you only can use `easy_install` than use

.. code-block:: console

   $ easy_install Flask-fillin

.. _pip: http://pip.openplans.org/

Flask-fillin requires to run some packages (they will be installed automatically if they not already installed):

* Flask
* lxml

First form testing
==================

It is very simple now to test a received form by filling out.::

   from flask.ext.fillin import FormWrapper
   from flask.testing import FlaskClient

   client = FlaskClient(flask_app, response_wrapper=FormWrapper)
   response = client.get('/page_with_form')
    
   response.form.fields['username'] = 'my username'
   response.form.fields['password'] = 'secret'
   response.form.fields['remember'] = True
    
   response.form.submit(client)

You can see that we extends the default :class:`~flask.testing.FlaskClient` with the :class:`~flask.ext.FormWrapper` of fillin. This wrapper extends the response class with the parameter **forms** and **form**.

In this you can find the forms of your page and you are able to fill in your test data. Than you can submit the form and check the new response on validity.

For more examples and use cases look inside the tests.py and test_app in the git repository.

API Documentation
=================

.. autoclass:: FormWrapper
    :members: