#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import (
    Flask,
    render_template,
    request,
)
import ConfigParser


#init config
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
app = Flask(config.get('dancebo', 'app_name'))
app.secret_key = config.get('dancebo', 'secret_key')
debug = bool(config.get('dancebo', 'debug'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return str(request.form)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=debug)
