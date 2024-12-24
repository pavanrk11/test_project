
import pytest

from my_package.module import add, subtract, multiply, divide

@pytest.fixture(scope="module")
def resource():
    # Setup
    print("Setup resource")
    yield "resource_data"
    # Teardown
    print("Teardown resource")


def test_tests1(resource):

    # add
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    # subtract
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4

    # multiply
    assert multiply(3, 5) == 15
    assert multiply(0, 100) == 0
    assert multiply(-2, 4) == -8

    # divide
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(7, 1) == 7

    # Testing division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_tests():

    # add
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    # subtract
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4

    # multiply
    assert multiply(3, 5) == 15
    assert multiply(0, 100) == 0
    assert multiply(-2, 4) == -8

    # divide
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(7, 1) == 7

    # Testing division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)