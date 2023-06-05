import pytest

from src.vacancy import Vacancy


@pytest.fixture
def fixture_vacancy():
    return Vacancy(1, 'Python', 'url', '1000','2000', 'fixture_vacancy', 'hh', 'area', 'currency')

def test_vacancy_init(fixture_vacancy):
    assert fixture_vacancy.id_vacancy == 1
    assert fixture_vacancy.title == "Python"
    assert fixture_vacancy.url == "url"
    assert fixture_vacancy.salary_from == '1000'
    assert fixture_vacancy.salary_to == '2000'
    assert fixture_vacancy.employer == "fixture_vacancy"
    assert fixture_vacancy.platform == "hh"
    assert fixture_vacancy.area == "area"
    assert fixture_vacancy.currency == "currency"

def test__repr__(fixture_vacancy):
    assert repr(fixture_vacancy) == '<Vacancy id=1 title=Python salary_from=1000 salary_to=2000 ''employer=fixture_vacancy platform=hh area=area currency=currency>'


def test__str__(fixture_vacancy):
    assert str(fixture_vacancy) == 'Python\n''Salary_from: 1000 Salary_to: 2000 Currency: currency,\n''Employer: fixture_vacancy,\n''Platform: hh\n''Area: area'