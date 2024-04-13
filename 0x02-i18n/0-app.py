#!/usr/bin/env python3
"""
A simple Flask application serving a basic HTML template.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
