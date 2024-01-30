import json

from requests import get
from src.abc_api.abc_job_api import JobApi


class GetInfoSJ(JobApi):
    _url = 'https://api.superjob.ru/2.0/vacancies/'
    _api_key = 'v3.r.137746496.a21f57366f1feb189619dcc5f50ea79c00001abd.a2c3957b66dd1205e59f39b61529f8bc8af25cc3'

    def __init__(self):
        pass

    def __str__(self):
        return 'HeadHunter.ru'

    def get_vacancies_api(self, key_word):
        params = {'keyword': key_word}
        headers = {
            'X-Api-App-Id': self._api_key
        }
        response = get(self._url, headers=headers, params=params)
        # print(response.url)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            return data_dict
        else:
            print(response.status_code)
            return None

    def get_formatted_data(self, vacancies):
        formatted_data = []
        for vacancy in vacancies['objects']:
            formatted_data.append({
                'title': vacancy['profession'],
                'url': vacancy['link'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to'],
                'requirement': vacancy['candidat']
            })
        return formatted_data

# sj = GetInfoSJ()
# print(sj.get_vacancies_api('Python'))
