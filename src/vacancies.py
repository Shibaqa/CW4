class Vacancies:

    def __init__(self, title, url, salary_from, salary_to, requirement):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    def __str__(self):
        return f'Должность: {self.title}\n' \
               f'Ссылка на вакансию: {self.url}\n' \
               f'Зарплата: {self.salary_from} - {self.salary_to} руб.\n' \
               f'Требования: {self.requirement}\n'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from
