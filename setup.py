"""
Flask-fillin
------------

This Flask extension provides simple utilities for testing your forms in 
Flask application.

Links
`````

* `documentation <http://packages.python.org/Flask-fillin>`_
* `development version <http://github.com/jarus/flask-fillin/zipball/master#egg=Flask-fillin-dev>`_
* `Flask <http://flask.pocoo.org>`_

"""
from setuptools import setup


setup(
    name='Flask-fillin',
    version='0.2',
    url='http://github.com/jarus/flask-fillin/',
    license='BSD',
    author='Christoph Heer',
    author_email='christoph.heer@googlemail.com',
    description='A flask extension that provides utilities to test forms.',
    long_description=__doc__,
    packages=['flask_fillin'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'lxml'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)