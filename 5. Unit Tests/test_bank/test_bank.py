from bank import value

def test_value_0():
    assert value("hello") == 0

def test_value_0_entire():
    assert value("Hello, Newman") == 0

def test_value_20():
    assert value("how you doing?") == 20

def test_value_100():
    assert value("What's up") == 100
    assert value("What's happening?") == 100