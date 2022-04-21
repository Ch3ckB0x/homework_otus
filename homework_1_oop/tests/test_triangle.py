import pytest

from homework_1_oop.src.Triangle import Triangle
from homework_1_oop.src.Figure import Figure


def test_isinstance_triangle():
    if isinstance(Triangle(2, 4, 5), Figure):
        assert True
    else:
        assert False


@pytest.mark.parametrize("a,b,c", [(-4, 4, 5),
                                   (3, -7, 8),
                                   (4, 4, -5)])
def test_init_exception_triangle_zero(a, b, c):
    with pytest.raises(ValueError, match="Sides should be > 0"):
        Triangle(a, b, c)


@pytest.mark.parametrize("a,b,c", [(1, 2, 3)])
def test_init_exception_triangle_no_exists(a, b, c):
    with pytest.raises(ValueError, match="No such triangle exists"):
        Triangle(a, b, c)


@pytest.mark.parametrize("a,b,c,expected_result", [(4, 3, 5, 6),
                                                   (2.7, 4.2, 3.3, 4.45)])
def test_get_area_square(a, b, c, expected_result):
    area_triangle = Triangle(a, b, c).area
    assert area_triangle == expected_result


@pytest.mark.parametrize("a,b,c,expected_result", [(4, 3, 5, 12),
                                                   (2.7, 4.2, 3.3, 10.2)])
def test_get_perimeter_rectangle(a, b, c, expected_result):
    perimeter_triangle = Triangle(a, b, c).perimeter
    assert perimeter_triangle == expected_result
