from abc import ABC

class AbstractMovieRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError