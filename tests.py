# -*- coding: utf-8 -*-
"""
    flask-fillin-tests
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Christoph Heer.
    :license: BSD, see LICENSE for more details.
"""

import unittest

from test_app import app

from flask.testing import FlaskClient
from flask.ext.fillin import FormWrapper

class fillinTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = FlaskClient(self.app, response_wrapper=FormWrapper)

    def tearDown(self):
        pass
    
    def test_login_form(self):
        response = self.client.get('/login-form')
        response.form.fields['username'] = "test"
        assert 'Missing password' in response.form.submit(self.client).data
        
        response = self.client.get('/login-form')
        response.form.fields['password'] = "secret"
        assert 'Missing username' in response.form.submit(self.client).data
        
        response = self.client.get('/login-form')
        response.form.fields['username'] = "test"
        response.form.fields['password'] = "secret"
        assert 'Welcome test' in response.form.submit(self.client).data
        
    def test_data_injection(self):
        response = self.client.get('/login-form')
        response.form.fields['password'] = "secret"
        
        inject_data = {'username': 'test'}
        response = response.form.submit(self.client, data=inject_data)
        assert 'Welcome test' in response.data
    
    def test_hidden_field_form(self):
        response = self.client.get('/hidden-field-form')
        
        response = response.form.submit(self.client)
        assert 'Hidden field received' in response.data
        
        response = self.client.post('/hidden-field-form')
        assert 'Missing the hidden field' in response.data

    def test_checkbox_form(self):
        response = self.client.get('/checkbox-field-form')
        
        response = response.form.submit(self.client)
        assert "Checkbox did not check" in response.data
        
        response.form.fields['checkbox_field'] = True
        response = response.form.submit(self.client)
        assert "Checkbox checked" in response.data
        
    def test_links_get(self):
        response = self.client.get('/link')
        
        self.assertEquals(2, len(response.links()), '2 links are parsed from the source')
        self.assertEquals('link1', response.link('#link1').text)
        self.assertEquals('link2', response.link('.link').text)
        
    def test_link_click(self):
        response = self.client.get('/link')
        
        response = response.link("#link1").click(self.client)
        self.assertEquals(200, response.status_code)
        
if __name__ == '__main__':
    unittest.main()