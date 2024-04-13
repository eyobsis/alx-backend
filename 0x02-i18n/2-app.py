#!/usr/bin/env python3
"""
A basic Flask application with Babel setup and locale selector.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Config class for available languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()
