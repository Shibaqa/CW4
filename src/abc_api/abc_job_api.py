from abc import ABC, abstractmethod


class JobApi(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_vacancies_api(self):
        pass
