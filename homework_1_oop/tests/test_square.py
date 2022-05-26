import pytest

from homework_1_oop.src.Square import Square
from homework_1_oop.src.Figure import Figure


def test_isinstance_square():
    if isinstance(Square(2), Figure):
        assert True
    else:
        assert False


@pytest.mark.parametrize("side", [0, -3])
def test_init_exception_square(side):
    with pytest.raises(ValueError, match="Side should be > 0"):
        Square(side)


@pytest.mark.parametrize("side,expected_result", [(4, 16),
                                                  (2.5, 6.25)])
def test_get_area_square(side, expected_result):
    area_square = Square(side).area
    assert area_square == expected_result


@pytest.mark.parametrize("side,expected_result", [(3, 12),
                                                  (1.5, 6)])
def test_get_perimeter_rectangle(side, expected_result):
    perimeter_square = Square(side).perimeter
    assert perimeter_square == expected_result
