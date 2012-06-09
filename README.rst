============
Flask-fillin
============

This Flask extension provides simple utilities for **testing your forms** in 
Flask application.

Installation
============
The installation is thanks to the Python Package Index and `pip`_ really simple.

::

   $ pip install Flask-fillin

If you only can use `easy_install` than use

::

   $ easy_install Flask-fillin

.. _pip: http://pip.openplans.org/

Flask-fillin requires to run some packages (they will be installed automatically if they not already installed):

* Flask
* lxml

Example Usage
=============

::

   from flask.ext.fillin import FormWrapper

   client = FlaskClient(flask_app, response_wrapper=FormWrapper)
   
   # form submission
   response = client.get('/page_with_form')
   
   response.form.fields['username'] = 'my username'
   response.form.fields['password'] = 'secret'
   response.form.fields['remember'] = True
   
   response.form.submit(client)

   # link navigation
   response = client.get('/page_with_links')
   response.link("#link-id").click(client)

   # underlying parsed html
   links = response.html.findall("a")