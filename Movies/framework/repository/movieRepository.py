from typing import List

from Movies.Entity.Movie import Movie
from Movies.framework.database.connection import Connection


class MovieRepository:
    def __init__(self, connection: Connection ):
        self.connection = connection

    def get_by_id(self, movie_id: int):
        self.connection.query("SELECT * FROM movies where movie_id = ?", [movie_id])

    def get_all(self) -> List[Movie]:
        results = self.connection.query("SELECT * FROM movies", []).fetchall()

        movies_list: List[Movie] = []

        for result in results:
            movies_list.append(Movie(result[0], result[1]))

        return movies_list

    def create(self, movieDict) -> Movie:
        self.connection.query("INSERT INTO movies(movie_name) VALUES (?)", [movieDict['name']])
        self.connection.getLastRowId()
        self.connection.commit()

        return Movie(
            self.connection.getLastRowId(),
            movieDict['name']
        )