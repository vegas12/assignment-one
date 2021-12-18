from flask import Flask
from Movies import main

app = Flask(__name__)

app.register_blueprint(main.movies, url_prefix="/api/movies")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"