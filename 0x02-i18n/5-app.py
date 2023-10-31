#!/usr/bin/env python3
"""Create a simple flask appication"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import List, Dict, Union

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """Create babel configurations"""

    LANGUAGES: List = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """set a global user if signed in"""
    user: Dict = get_user()
    if user:
        g.user = user


@app.route('/')
def index():
    """Return index.html"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """Return the language selection to use"""
    locale: str = request.args.get('locale')
    if locale in ['fr', 'en']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[str, None]:
    """Return a user dictionary"""
    user_id: int = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    app.run()
