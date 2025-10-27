from utils import *

class DIR(BINARY):
    UP = 1
    DN = -1

def test_negation():
    assert -DIR.UP is DIR.DN
    assert -DIR.DN is DIR.UP

def test_int_values():
    assert 1 == DIR.UP
    assert -1 == DIR.DN
    assert DIR.UP == 1
    assert DIR.DN == -1
    assert int(DIR.UP) == 1
    assert int(DIR.DN) == -1

def test_str_values():
    assert str(DIR.UP) == "UP"
    assert str(DIR.DN) == "DN"

def test_access_by_square_brackets():
    assert DIR["UP"] is DIR.UP 
    assert DIR["DN"] is DIR.DN

def test_access_by_parentheses():
    assert DIR(1) is DIR.UP
    assert DIR(-1) is DIR.DN

def test_none():
    assert DIR[None] is None
    assert DIR(None) is None