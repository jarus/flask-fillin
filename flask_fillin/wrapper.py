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
        
        Adds also :data:`html` which is parsed lxml HtmlElement and methods
        :data:`link` and :data:`links` for link access.
        
        Each link has method click(client) which calls client.get(href).
    """
        
    _parsed_html = None
    
    @property
    def html(self):
        if self._parsed_html is None:
            self._parsed_html = document_fromstring(self.data)
            response = self
            
            # add click function to all links
            def _click(self, client, **kwargs):
                path = self.attrib['href']
                return client.get(path, **kwargs)
            
            for link in self._parsed_html.iter('a'):
                setattr(link, 'click', types.MethodType(_click, link))
            
            # add submit function to all links
            def _submit(self, client, path=None, **kargs):
                data = dict(self.form_values())
                if kargs.has_key('data'):
                    data.update(kargs['data'])
                    del kargs['data']
                if path is None:
                    path = self.action
                    if path == "":
                        print dir(response)
                        print response.response
                if not kargs.has_key('method'):
                    kargs['method'] = self.method
                return client.open(path, data=data, **kargs)
                
            for form in self._parsed_html.forms:
                setattr(form, "submit", types.MethodType(_submit, form))
        return self._parsed_html
    
    @property
    def forms(self):
        """A list of all received forms in the same way like 
        `lxml <http://lxml.de/lxmlhtml.html#forms>`_ with the same functions 
        and an additional function to submit the form over a test client.
        """
        return self.html.forms
    
    @property
    def form(self):
        """The first received form from the page."""
        return self.forms[0]
    
    def links(self, css_expression="a"):
        """Get all the links by css_express"""
        return self.html.cssselect(css_expression)
        
    def link(self, css_expression="a"):
        """Get first link by css_expression"""
        links = self.links(css_expression)
        if links:
            return links[0]
