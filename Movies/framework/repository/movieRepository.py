from Movies.interface.abstractMovieRepository import AbstractMovieRepository


class MovieRepository(AbstractMovieRepository):
    def get_by_id(self, movie_id: int):
        print("get_by_id")