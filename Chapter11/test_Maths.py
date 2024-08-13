
from Maths import division

def test_division_whenInputIsValid_ShouldReturnRightValue():
    # arrange
    a = 2
    b = 2

    # act
    result = division(a, b)

    # assert
    assert result == 1


def test_division_whenInputIsNotANumber_ShouldRaiseValueError():
    # arrange
    a = "a"
    b = 2

    # act and assert
    try:
        division(a, b)
        assert False
    except ValueError:
        assert True

