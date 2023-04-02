import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity >= 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(6)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(5)