# coding: utf8
from flask import (
    render_template,
    session,
    request,
    redirect,
)
from flask.views import View
from werkzeug.exceptions import Forbidden
from models.user import UserModel


class Misc(View):

    def show_home(self):
        home_data = UserModel().generic_stats()
        invoices_to_generate = UserModel().invoices_to_edit()
        return render_template(
            'home.html',
            current_page="home",
            stats=home_data,
            invoices=invoices_to_generate
        )

    def login(self):
        if session.get('name'):
            return redirect('/home')
        if request.method == 'POST':
            print request.form
            # if not password == request.form['password']:
            #     raise Forbidden('You don\'t have access to this ressource')
            session['name'] = request.form['login']
            return redirect('/home')
        return render_template('login.html')
