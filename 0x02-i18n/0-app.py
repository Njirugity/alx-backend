#!/usr/bin/env python3
""" A script for basic flask integration"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route('/')
def index():
    """This function returns the
    rendered template for the index
    html page.
    Returns:
        The rendered template for the index.html page.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
