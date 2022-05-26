import pytest

from homework_1_oop.src.Circle import Circle
from homework_1_oop.src.Figure import Figure


def test_isinstance_circle():
    if isinstance(Circle(1), Figure):
        assert True
    else:
        assert False


def test_init_exception_circle():
    with pytest.raises(ValueError, match="Radius should be > 0"):
        Circle(-5)


@pytest.mark.parametrize("radius,expected_result", [(5, 78.54),
                                                    (33.48, 3521.44),
                                                    (0, 0)])
def test_get_area_circle(radius, expected_result):
    area_circle = Circle(radius).area
    assert area_circle == expected_result


@pytest.mark.parametrize("radius,expected_result", [(10, 62.83),
                                                    (3.87, 24.32),
                                                    (0, 0)])
def test_get_perimeter_circle(radius, expected_result):
    perimeter_circle = Circle(radius).perimeter
    assert perimeter_circle == expected_result
