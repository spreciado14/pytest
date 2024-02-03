from math_utils import MathUtils

def test_add():
    # Test cases
    result = MathUtils.add(3, 5)
    assert result == 8

    result = MathUtils.add(2, 8)
    assert result == 10

    result = MathUtils.add(0, 0)
    assert result == 0

def test_subtract():
    result = MathUtils.subtract(5, 3)
    assert result == 2

    result = MathUtils.subtract(7, 2)
    assert result == 5

    result = MathUtils.subtract(0, 0)
    assert result == 0

def test_multiply():
    result = MathUtils.multiply(5, 3)
    assert result == 15

    result = MathUtils.multiply(7, 2)
    assert result == 14

    result = MathUtils.multiply(0, 0)
    assert result == 0

def test_divide():
    result = MathUtils.divide(5, 3)
    assert result == 1.6666666666666667

    result = MathUtils.divide(7, 2)
    assert result == 3.5

    result = MathUtils.divide(0, 0)
    assert result == -1.0

test_divide()
test_add()
test_subtract()
test_multiply()