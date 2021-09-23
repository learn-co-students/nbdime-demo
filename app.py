from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_name(name):
    return f"<p>Hello, {name}!</p>"

from waitress import serve
serve(app, host='0.0.0.0', port=5000)