import json
from src.abc_api.abc_job_api import JobApi
from requests import get


class GetInfoHH(JobApi):
    _url = 'https://api.hh.ru/vacancies/'

    def __init__(self):
        pass

    def __str__(self):
        return 'HeadHunter.ru'

    def get_vacancies_api(self, key_word):
        params = {'text': key_word}
        response = get(self._url, params=params)

        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print(response.status_code)
            return None

    def get_formatted_data(self, vacancies):
        formatted_data = []
        for vacancy in vacancies['items']:
            salary_from, salary_to = None, None
            if vacancy['salary']:
                if vacancy['salary']['from']:
                    salary_from = vacancy['salary']['from']
                if vacancy['salary']['to']:
                    salary_to = vacancy['salary']['to']

            formatted_data.append({
                'title': vacancy['name'],
                'url': vacancy['alternate_url'],
                'salary_from': salary_from,
                'salary_to': salary_to,
                'requirement': vacancy['snippet']['requirement']
            })
        return formatted_data
