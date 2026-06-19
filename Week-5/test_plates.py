from plates import is_valid

def test_generic():
    assert is_valid("CS50P") == False
    assert is_valid("CS50X") == False
    assert is_valid("AAA22A") == False
    assert is_valid("NP023") == False
    assert is_valid("XP3230") == True
    assert is_valid("CSSS500") == False

def test_number_arrangement():
    assert is_valid("AB034") == False
    assert is_valid("KP543") == True
    assert is_valid("NS4340") == True
    assert is_valid("23343") == False

def test_special_char():
    assert is_valid("s.rk!") == False
    assert is_valid("!.tor") == False
    assert is_valid("!,no") == False
