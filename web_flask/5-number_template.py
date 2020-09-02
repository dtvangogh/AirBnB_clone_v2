#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Displays hello message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Displays the name of application
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """
        Displays C followed by text variable

    """
    return "C %s" % text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def pythonroute(text='is_cool'):
    """
        Displays C followed by text variable

    """
    return "Python %s" % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def int_only(n):
    """
        Displays number if int
    """
    return '%d is a number' % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def return_html_template(n):
    """render template"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
