import pytest
from bank import value

def test_upper_lower_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HeLlO") == 0
    assert value("hElLo") == 0

def test_hello_sentences():
    assert value("Hello, Mine.") == 0
    assert value("hello~ my sun~") == 0
    assert value("HeLLo! Good Moring!") == 0

def test_h_starting():
    assert value("Hey! what's going on?") == 20
    assert value("hehehehe... i got you~") == 20
    assert value("Hell in you mind!") == 20

def test_other_sentences():
    assert value("No way~") == 100
    assert value("What's are you doing?") == 100
    assert value("1..2..3.. Ready~ GO!") == 100

def test_empty_string():
    assert value("") == 100

def test_space():
    assert value(" ") == 100
