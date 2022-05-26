import pytest

from homework_1_oop.src.Rectangle import Rectangle
from homework_1_oop.src.Figure import Figure


def test_isinstance_rectangle():
    if isinstance(Rectangle(2, 4), Figure):
        assert True
    else:
        assert False


@pytest.mark.parametrize("side_a,side_b", [(-1, 2),
                                           (2, -1),
                                           (-2, -4),
                                           (0, 1),
                                           (1, 0),
                                           (0, 0)])
def test_init_exception_rectangle(side_a, side_b):
    with pytest.raises(ValueError, match="Sides should be > 0"):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("side_a,side_b,expected_result", [(2, 4, 8),
                                                           (3.48, 17.84, 62.08)])
def test_get_area_rectangle(side_a, side_b, expected_result):
    area_rectangle = Rectangle(side_a, side_b).area
    assert area_rectangle == expected_result


@pytest.mark.parametrize("side_a,side_b,expected_result", [(2, 4, 12),
                                                           (3.48, 17.84, 42.64)])
def test_get_perimeter_rectangle(side_a, side_b, expected_result):
    perimeter_rectangle = Rectangle(side_a, side_b).perimeter
    assert perimeter_rectangle == expected_result
