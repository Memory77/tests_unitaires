import pytest 
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5

def test_div():
    result = my_functions.div(number_one=1, number_two=4)
    assert result == 0.25

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.div(number_one=4, number_two=0)

def test_add_strings():
    result = my_functions.add("J'aime les ", "tests")
    assert result == "J'aime les tests"

def test_multiply_positive():
    result = my_functions.multiply(number_one=2, number_two=4)
    assert result == 8

def check_multiply_negative():
    result = my_functions.multiply(number_one=-2, number_two=4)
    assert result == -8

def test_multiply_by_zero():
    result = my_functions.multiply(number_one=2, number_two=0)
    assert result == 0

@pytest.mark.slow
def test_multiply_slow():
    time.sleep(5)
    result = my_functions.multiply(number_one=5, number_two=0)
    assert result == 0