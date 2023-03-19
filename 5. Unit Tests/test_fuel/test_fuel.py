from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

def test_convert_value():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("5/4")
        convert("x/y")
