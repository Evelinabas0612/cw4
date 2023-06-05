def sort_from_minimum_salary(data, reverse_data=False):
    """Функция сортировки по минимальной зарплате"""
    data = sorted(data, reverse=reverse_data)
    return data


def get_top_vacancies(vacancies_list, top_n):
    """Функция принимает отсортированный список вакансий и возвращает n-ое количество первых вакансий из списка"""

    top_vacancies = []
    count = 0
    while count < len(vacancies_list):
        top_vacancies.append(vacancies_list[count])
        count = count + 1

    return top_vacancies[:top_n]




