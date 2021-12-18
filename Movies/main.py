from flask import Flask
from flask import Blueprint

app = Flask(__name__)

movies = Blueprint("movies", __name__)

@movies.route('/')
def get_incomes():
  return "ASDASDa"
