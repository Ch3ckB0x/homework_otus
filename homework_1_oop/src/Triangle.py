from math import sqrt

from homework_1_oop.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides should be > 0")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("No such triangle exists")
        super().__init__()
        self.name = "Triangle"
        self.side_a = a
        self.side_b = b
        self.side_c = c

    @property
    def area(self):
        p = 1 / 2 * self.perimeter
        return round(sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2)

    @property
    def perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 2)
