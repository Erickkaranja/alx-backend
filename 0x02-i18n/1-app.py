#!/usr/bin/env python3
'''instanciating a simple flask application.'''

from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from config import Config
from typing import 
app = Flask(__name__)

babel = Babel(app)
app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    '''getting the most suitable locale.'''
    return request.accept_languages.best_match(Config['LANGUAGES'])

@app.route('/')
def index():
    '''returns 1-index.html file.'''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
