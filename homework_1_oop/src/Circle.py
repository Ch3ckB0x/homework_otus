from math import pi

from homework_1_oop.src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius should be > 0")
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    @property
    def area(self):
        return round(pi * self.radius ** 2, 2)

    @property
    def perimeter(self):
        return round(2 * pi * self.radius, 2)
