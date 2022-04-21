from homework_1_oop.src.Triangle import Triangle
from homework_1_oop.src.Square import Square


def test_add_area():
    square = Square(10)
    square.area
    triangle = Triangle(13, 14, 15)
    area = triangle.add_area(square)
    assert area == 184
