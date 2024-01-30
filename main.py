from src.hh import GetInfoHH
from src.superjob import GetInfoSJ
from src.data import InfoToJson
from src.vacancies import Vacancies

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = GetInfoHH()
superjob_api = GetInfoSJ()


def main():
    # Получение вакансий с разных платформ
    # HeadHunter
    user_key_word = input('Здравствуйте! Введите желаемую должность или сферу работы: ')
    hh_vacancies = hh_api.get_vacancies_api(user_key_word)
    hh_vacancies = hh_api.get_formatted_data(hh_vacancies)

    # SuperJob
    superjob_vacancies = superjob_api.get_vacancies_api(user_key_word)
    superjob_vacancies = superjob_api.get_formatted_data(superjob_vacancies)

    # Запись вакансий в json
    vacancies_dict = []
    vacancies_dict.extend(hh_vacancies)
    vacancies_dict.extend(superjob_vacancies)
    json_saver = InfoToJson(user_key_word)
    json_saver.add_vacancies(vacancies_dict)

    while True:
        user_input = input('''
        1 - Вывести все подходящие вакансии
        2 - Отсортировать по минимальной зарплате все подходящие вакансии
        3 - Если хотите отфильтровать вакансии по требованиям
        exit - выход :( 
        Ваш выбор: 
        ''')
        if user_input == '1':
            vacancies = json_saver.get_vacancies()
        if user_input == '2':
            vacancies = json_saver.sorted_vacancies()
        if user_input == '3':
            user_input_req = input('Требования к соискателю: ')
            vacancies = json_saver.filter_vacancies_requirement(user_input_req)
            if not vacancies:
                print('Нет вакансий, соответствующих заданным критериям :(')
                break
        if user_input == 'exit':
            break
        user_input_top_n = int(input('Введите количество вакансий для вывода в топ N: '))
        vacancies_top = vacancies[:user_input_top_n]
        for vacancy in vacancies_top:
            print(vacancy)


if __name__ == '__main__':
    main()
