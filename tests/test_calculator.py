import pytest

from calculator import add, divide, multiply, power, subtract


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), (-1, 1, 0), (0, 0, 0), (0.1, 0.2, 0.3),
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(-3, 3) == -9


def test_divide():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    assert power(2, 10) == 1024
