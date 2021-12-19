import json

from flask import Flask, Blueprint, g, jsonify, url_for
from flask_expects_json import expects_json

from Movies.Entity.Movie import Movie
from Movies.framework.database.connection import Connection
from Movies.framework.repository.movieRepository import MovieRepository

app = Flask(__name__)

movies = Blueprint("movies", __name__)

@movies.route('/', methods=['GET'])
def get_all():
  repository = MovieRepository(Connection('movies_database'))
  movies_list = repository.get_all()

  resp = jsonify([m.to_dict() for m in movies_list])

  return resp, 200

@movies.route('/<int:movie_id>', methods=['GET'])
def get_by_id(movie_id: int):
  repository = MovieRepository(Connection('movies_database'))
  result = repository.get_all()

  return str(len(result))

schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
  },
  "required": ["name"]
}
@movies.route('/', methods=['POST'])
@expects_json(schema)
def create_movie():
  repository = MovieRepository(Connection('movies_database'))

  created_movie = repository.create(g.data)

  resp = jsonify(created_movie.to_dict())
  resp.headers['Location'] = url_for('movies.get_by_id', movie_id=created_movie.movie_id)
  return resp, 201
