import json
from abc import ABC, abstractmethod

import vacancy
from exception import JSONException
from vacancy import Vacancy


class AbstractJSONSaver(ABC):
    """Абстрактный класс для работы с данными о вакансиях """

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def select(self):
        pass


class JSONSaver(AbstractJSONSaver):
    """Класс для работы с данными о вакансиях в json"""

    def __init__(self, keyword: str, name_file: str):
        self.__file = f"{keyword.title()}_{name_file.lower()}.json"

    @property
    def file(self):
        return self.file

    def add_vacancy(self, data):
        """Функция добавления вакансии в файл """
        try:
            with open(self.__file, 'w', encoding="UTF-8") as file_new:
                json.dump(data, file_new, indent=4, ensure_ascii=False)
        except JSONException(Exception):
            return 'JSON файл поврежден'

    def select(self):
        """Функция создает экземпляры класса Vacancy с заданными полями.
         Возвращает список вакансий
         """
        vacansies = []

        with open(self.__file, "r", encoding="UTF-8") as file_new:
            data = json.load(file_new)

        if "hh" in self.__file:
            for row in data:
                salary_from = 0
                salary_to = "не указано"
                currency = "не указано"
                if row["salary"]:
                    salary = row["salary"]
                    salary_from = salary["from"]
                    salary_to = salary["to"]
                    currency = salary["currency"]
                    if salary_from is None:
                        salary_from = 0
                    if salary_to is None:
                        salary_to = "не указано"
                    if currency is None:
                        currency = "не указано"

                vacansies.append(Vacancy(
                    row["id"],
                    row["name"],
                    row["url"],
                    salary_from,
                    salary_to,
                    row["employer"],
                    "hh",
                    row["area"],
                    currency))

        if "sj" in self.__file:
            for row in data:
                salary_from = 0
                salary_to = "не указано"
                currency = "не указано"
                if row["payment_from"]:
                    salary_from = row["payment_from"]
                    if salary_from is None:
                        salary_from = 0
                if row["payment_to"]:
                    salary_to = row["payment_to"]
                    if salary_to is None:
                        salary_to = "не указано"
                if row["currency"]:
                    currency = row["currency"]
                    if currency is None:
                        currency = "не указано"
                vacansies.append(Vacancy(
                    row["id"],
                    row["profession"],
                    row["link"],
                    salary_from,
                    salary_to,
                    row["client"],
                    "sj",
                    row["town"],
                    currency))

        return vacansies
