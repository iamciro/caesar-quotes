from flask import render_template
from caesar import app
from .utils import get_quote

@app.route('/')
def home():
    quote = get_quote()
    if quote:
        return render_template('index.html', quote=quote)
    return render_template('index.html', quote=None)
        