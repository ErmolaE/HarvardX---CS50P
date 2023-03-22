from numb3rs import validate

def test_validate_255():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1000.2.3.10") == False
    assert validate("1.2000.3.10") == False
    assert validate("1.2.350.10") == False

def test_validate_incorrect():
    assert validate("cat") == False
    assert validate("1.2") == False
    assert validate("205") == False
    assert validate("1.2.3") == False