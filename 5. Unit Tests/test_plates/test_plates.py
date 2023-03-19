from plates import is_valid

def test_start_2lett():
    assert is_valid("50") == False
    assert is_valid("CS50") == True

def test_zero():
    assert is_valid("CS05") == False

def test_middle_numbers():
    assert is_valid("CS50P") == False

def test_marks():
    assert is_valid("PI3.14") == False

def test_len():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False