from datetime import date
from seasons import get_date, get_age

def test_get_date():
    assert get_date("2022-4-1") == date(2022, 4, 1)

def test_get_age():
    assert get_age(date(2022, 4, 1), date(2023, 4, 1)) == "Five hundred twenty-five thousand, six hundred"