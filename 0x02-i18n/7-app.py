#!/usr/bin/env python3
"""Create a simple flask appication"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from typing import List, Dict

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
def index() -> str:
    """Return index.html"""
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> str:
    """Return the language selection to use"""
    locale: str = app.config['BABEL_DEFAULT_LOCALE']
    try:
        if request.headers.get('locale'):
            if request.headers.get('locale') in app.config['LANGUAGES']:
                locale = request.headers.get('locale')
        if hasattr(g, 'user'):
            if g.user['locale'] in app.config['LANGUAGES']:
                locale = g.user['locale']
        if request.args.get('locale'):
            if request.args.get('locale') in app.config['LANGUAGES']:
                locale = request.args.get('locale')
        return locale
    except AttributeError:
        pass


@babel.timezoneselector
def get_timezone() -> str:
    """Return the current timezone"""
    tz: str = app.config['BABEL_DEFAULT_TIMEZONE']
    if hasattr(g, 'user'):
        tz = g.user['timezone']
    if request.args.get('timezone'):
        tz = request.args.get('timezone')
    try:
        pytz.timezone(tz)
        return tz
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user() -> Dict:
    """Return a user dictionary"""
    user_id: int = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    app.run()
