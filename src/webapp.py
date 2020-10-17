#!/usr/bin/env python3
import os
import json
import sqlite3

from flask import (
    g, Flask, render_template,
)
import click

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from config import Config
import random_horror


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


DATABASE = 'random_horror_001.sq3'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app = Flask("Random-Horror")


@app.route('/login')
def login():
    outhtml = ""
    outhtml += render_template('login.html', form=LoginForm())
    return outhtml


@app.route('/random/<num>', methods=['GET'])
def index(num=3):
    horrors = json.loads(random_horror.randomise(int(num), True))
    outhtml = ""
    outhtml += render_template(
        'roll_result.html',
        horrors=horrors,
        stylesheets=['style.css']
    )
    return outhtml


@click.command()
@click.option('--host', '-h', 'host', type=str,
              default="127.0.0.1", show_default=True,
              help='Specify host to listen on.')
@click.option('--port', '-p', 'port', type=int,
              default=8800, show_default=True,
              help='Specify port to listen on.')
@click.option('--debug', '-D', 'app_debug',
              is_flag=True, default=False, show_default=True,
              help='Enable Debug mode. Code changes are picked-up.')
def main(host, port, app_debug):
    app.config.from_object(Config)
    if app_debug:
        click.secho("!!! App Debugging Enabled !!!", fg="blue")
        click.secho(f"!!! [ PID: { os.getpid() } ] !!!", fg="yellow", bold=True)
    app.run(host=host, port=port, debug=app_debug)


if __name__ == '__main__':
    main()
