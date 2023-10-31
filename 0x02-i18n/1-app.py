#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from config import Config

app = Flask(__name__)

babel = Babel(app)
app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
