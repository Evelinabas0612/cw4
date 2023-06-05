# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.job_api import HeadHunterAPI, SuperJobAPI
from src.json_saver import JSONSaver
from src.utils import sort_from_minimum_salary, get_top_vacancies


def user_interaction():
    """Функция диалога с пользователем"""

    print('Добро пожаловать! Это сервис по поиску вакансий на HeadHunter и SuperJob')
    search_query = input("Введите поисковый запрос: ")

    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()

    vacancies_hh = hh_api.get_vacancies(search_query)
    vacancies_sj = sj_api.get_vacancies(search_query)

    json_saver_hh = JSONSaver(search_query, "hh")
    json_saver_hh.add_vacancy(vacancies_hh)

    json_saver_sj = JSONSaver(search_query, "sj")
    json_saver_sj.add_vacancy(vacancies_sj)

    print('Выберите команду: ')
    while True:
        vacancies_json = []
        command = input(
            '1 - Вывести список вакансий hh;\n'
            '2 - Вывести список вакансий sj;\n'
            '3 - Сортировать по минимальной зарплате hh;\n'
            '4 - Сортировать по минимальной зарплате sj;\n'
            '5 - Вывести top-вакансий hh;\n'
            '6 - Вывести top-вакансий sj;\n'
            'exit - Выход;\n'
        )
        if command.lower() == 'exit':
            print("До свидания!")
            break
        elif command == '1':
            vacancies_json = json_saver_hh.select()
        elif command == '2':
            vacancies_json = json_saver_sj.select()
        elif command == '3':
            vacancies_json = sort_from_minimum_salary(json_saver_hh.select(), True)
        elif command == '4':
            vacancies_json = sort_from_minimum_salary(json_saver_sj.select(), True)
        elif command == '5':
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            vacancies_json = get_top_vacancies(sort_from_minimum_salary(json_saver_hh.select(), True), top_n)
        elif command == '6':
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            vacancies_json = get_top_vacancies(sort_from_minimum_salary(json_saver_sj.select(), True), top_n)
        else:
            print("Выберите команду из списка или наберите exit")

        for vacancy in vacancies_json:
            print(vacancy, end='\n\n')


if __name__ == "__main__":
    user_interaction()
