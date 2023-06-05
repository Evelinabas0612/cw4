class ParsingError(Exception):
    """Класс для обработки исключения, если ошибка получения данных по API"""

    def __str__(self):
        return 'Ошибка получения данных по API'

class JSONException(Exception):
    """Класс для обработки исключения, если файл поврежден"""

    def __str__(self):
        return 'JSON файл поврежден'
