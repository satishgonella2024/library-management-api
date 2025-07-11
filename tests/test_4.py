import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def test_divide_happy_path():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError) as e:
        divide(10, 0)
    assert str(e.value) == "Division by zero"

def test_divide_large_numbers():
    assert divide(10**10, 2) == 5e9