#!/usr/bin/python3
from web_flask import app


@app.route('/python/<text>', strict_slashes=False)
def get_text_py(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')