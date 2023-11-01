#!/usr/bin/env python3
'''instanciating a simple flask application.'''

from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from config import Config

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

SUPPORTED_LANGUAGES = Config.LANGUAGES


@babel.localeselector
def get_locale() -> str:
    '''finding the most suitable locale.'''
    accepted_languages = request.accept_languages

    for lang in accepted_languages:
        if lang.language in SUPPORTED_LANGUAGES:
            return lang.language

    return 'en'


@app.route('/')
def index():
    '''rendering 3-index.html file.'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
