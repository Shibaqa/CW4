import json
from abc import ABC, abstractmethod
from src.vacancies import Vacancies


class DataVacancies(ABC):

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass


class InfoToJson:

    def __init__(self, key_word):
        self.filename = f'{key_word}.json'

    def add_vacancies(self, data):
        with open(self.filename, 'w', encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        with open(self.filename, 'r', encoding="UTF-8") as file:
            vacancies = json.load(file)
            vacancies = [Vacancies(x['title'], x['url'], x['salary_from'], x['salary_to'], x['requirement']) for x in
                         vacancies]
        return vacancies

    def sorted_vacancies(self):
        vacancies = self.get_vacancies()
        return sorted(vacancies, key=lambda x: x.salary_from if x.salary_from else 0)

    def filter_vacancies_requirement(self, filter_word):
        vacancies = self.get_vacancies()
        filtered_vacancies = []
        for vacancy in vacancies:
            if filter_word in vacancy.requirement:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies
