from flask import Flask, Blueprint, g, jsonify, url_for
from flask_expects_json import expects_json

from Movies.framework.database.connection import Connection
from Movies.framework.repository.movieRepository import MovieRepository

movies = Blueprint("movies", __name__)

@movies.route('/', methods=['GET'])
def get_all():
  repository = MovieRepository(Connection('movies_database'))
  movies_list = repository.get_all()

  resp = jsonify([movie.to_dict() for movie in movies_list])

  return resp, 200

@movies.route('/<int:movie_id>', methods=['GET'])
def get_by_id(movie_id: int):
  repository = MovieRepository(Connection('movies_database'))
  movie = repository.get_by_id(movie_id)

  resp = jsonify(movie.to_dict())

  return resp, 200

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
