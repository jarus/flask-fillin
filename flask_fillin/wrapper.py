# -*- coding: utf-8 -*-
"""
    flask.ext.fillin.wrapper
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Add modifiy response class with form parsing support.

    :copyright: (c) 2012 by Christoph Heer.
    :license: BSD, see LICENSE for more details.
"""

import types

from flask.wrappers import Response
from lxml.html import document_fromstring

class FormWrapper(Response):
    """An additional wrapper for the :class:`~flask.testing.FlaskClient` which 
    adds :data:`form` and :data:`forms` as parameter of the response.::

        from flask.ext.fillin import FormWrapper

        client = FlaskClient(flask_app, response_wrapper=FormWrapper)
        response = client.get('/page_with_form')
    
        response.form.fields['username'] = 'my username'
        response.form.fields['password'] = 'secret'
        response.form.fields['remember'] = True
    
        response.form.submit(client)
    """
        
    _parsed_html = None
    
    @property
    def forms(self):
        """A list of all received forms in the same way like 
        `lxml <http://lxml.de/lxmlhtml.html#forms>`_ with the same functions 
        and an additional function to submit the form over a test client.
        """
        if self._parsed_html is None:
            self._parsed_html = document_fromstring(self.data)
            
        def _submit(self, client, **kargs):
            data = dict(self.form_values())
            if kargs.has_key('data'):
                data.update(kargs['data'])
                del kargs['data']
            return client.open(self.action, method=self.method, data=data,
                               **kargs)
        
        for form in self._parsed_html.forms:
            setattr(form, "submit", types.MethodType(_submit, form))
            
        return self._parsed_html.forms
    
    @property
    def form(self):
        """The first received form from the page."""
        return self.forms[0]