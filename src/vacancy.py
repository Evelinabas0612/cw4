class Vacancy:
    """
    Класс вакансии
    """

    def __init__(self, id_vacancy, title, url, salary_from, salary_to, employer, platform, area, currency):
        self.id_vacancy = id_vacancy
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.platform = platform
        self.area = area
        self.currency = currency

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self.salary_from is not None and other.salary_from is not None:
                return self.salary_from > other.salary_from
        return "Некорректные данные для сравнения"

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __repr__(self):
        return f"<Vacancy id={self.id_vacancy} title={self.title} url={self.url} salary_from={self.salary_from} salary_to={self.salary_to} employer={self.employer} platform={self.platform} area={self.area} currency={self.currency}>"

    def __str__(self):
        return f"{self.title}\nURL: {self.url}\nSalary_from: {self.salary_from} Salary_to: {self.salary_to} Currency: {self.currency},\nEmployer: {self.employer},\nPlatform: {self.platform}\nArea: {self.area}"
