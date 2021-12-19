from typing import TypedDict


class MovieDict(TypedDict):
    id: int
    name: str


class Movie:
    def __init__(self, movie_id: int, name: str):
        self.movie_id = movie_id
        self.name = name

    def get_id(self):
        return self.movie_id

    def get_name(self):
        return self.name

    def to_dict(self) -> MovieDict:
        return {
            "id": self.movie_id,
            "name": self.name
        }