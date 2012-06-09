# -*- coding: utf-8 -*-
"""
    flask-fillin-test-app
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Christoph Heer.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/login-form", methods=["GET", "POST"])
def login_form():
    msg = None
    if request.method == "POST":
        if not request.form.has_key('username'):
            msg = "Missing username"
        if not request.form.has_key('password'):
            msg = "Missing password"
        
        if not msg:
            msg = "Welcome " + request.form.get('username')
    
    return render_template("login_form.html", msg=msg)

@app.route("/hidden-field-form", methods=["GET", "POST"])
def hidden_field_form():
    msg = None
    if request.method == "POST":
        if not request.form.has_key('hidden_field'):
            msg = "Missing the hidden field"
        else:
            msg = "Hidden field received"
    
    return render_template("hidden_field_form.html", msg=msg)

@app.route("/checkbox-field-form", methods=["GET", "POST"])
def checkbox_field_form():
    msg = None
    if request.method == "POST":
        if request.form.get('checkbox_field', False):
            msg = "Checkbox checked"
        else:
            msg = "Checkbox did not check"
    
    return render_template("checkbox_field_form.html", msg=msg)

@app.route('/link')
def link():
    return render_template('link.html')

@app.route("/form-without-action", methods=["GET", "POST"])
def from_without_action():
    msg = None
    if request.method == "POST":
        msg = "Submit success without action url"
    return render_template("form_without_action.html", msg=msg)

if __name__ == "main":
    app.run()
