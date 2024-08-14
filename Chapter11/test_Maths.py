"""
Fixture example
"""

import pytest
from maths import Maths

# define fixture for maths
@pytest.fixture
def maths():
    # put the setup code here
    decimals = 3
    maths = Maths(decimals)
    return maths


def test_division_whenInputIsValid_ShouldReturnRightValue(maths):
    # arrange
    a = 2
    b = 2

    # act
    result = maths.division(a, b)

    # assert
    assert result == 1


def test_division_whenInputIsNotANumber_ShouldRaiseValueError(maths):
    # arrange
    a = "a"
    b = 2

    # act and assert
    try:
        maths.division(a, b)
        assert False
    except ValueError:
        assert True


def test_division_whenInputValid_shouldReturnGoodDecimalPrecision(maths):
    # arrange
    a = 2
    b = 3

    # act
    result = maths.division(a, b)

    # assert
    # presicion is 3
    assert result == 0.667