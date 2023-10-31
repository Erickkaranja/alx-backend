#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from config import Config

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)
app.config.from_object(Config)

SUPPORTED_LANGUAGES = Config.LANGUAGES

@babel.localeselector
def get_locale():
    if 'locale' in request.args and request.args['locale'] in SUPPORTED_LANGUAGES:
        return request.args['locale']

    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)
    

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
