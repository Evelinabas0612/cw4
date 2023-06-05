import os
from abc import ABC, abstractmethod

import requests

from exception import ParsingError


class AbstractJobAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_request(self):
        pass


class HeadHunterAPI(AbstractJobAPI):

    def get_request(self,search_query):
        """Метод делает запрос на https://api.hh.ru/vacancies и возвращает результат в формате json"""

        url = 'https://api.hh.ru/vacancies'
        params = {
            "text": search_query,
            "page": None,
            "per_page": 10,
            "archived": False,
        }

        response = requests.get(url,
                                params=params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['items']

    def get_vacancies(self, search_query):
        return self.get_request(search_query)


class SuperJobAPI(AbstractJobAPI):

    def get_request(self, search_query):
        """Метод делает запрос на https://api.superjob.ru/2.0/vacancies/ и возвращает результат в формате json"""

        url = 'https://api.superjob.ru/2.0/vacancies/'
        params = {
            'keyword': search_query,
            "page": None,
            "per_page": 10,
            "archived": False,
        }
        headers = {
            'X-Api-App-Id': 'v3.r.137591220.8c54812be34ad4158bce9b07889e520d925ba06c.4d0ffd3e5e8b8e765c2fc32b62e499482d340be8'
        }

        response = requests.get(url,
                                params=params, headers=headers)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['objects']

    def get_vacancies(self, search_query):
        """
        Возвращает вакансии по ключевому слову
        :param keyword: ключевое слово пользователя
        """
        return self.get_request(search_query)
