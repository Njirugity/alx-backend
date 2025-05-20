#!/usr/bin/env python3
""" A script for basic flask integration"""

from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request

app = Flask(__name__)


class Config:
    """
    Configuration class for the application.
        Attributes:
        Languages (list): List of supported languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'utc'


app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """
    Handles / route
    """
    return render_template('4-index.html', home_title=_("home_title"), home_header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)
