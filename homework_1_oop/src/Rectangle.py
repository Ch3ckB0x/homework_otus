from homework_1_oop.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if (side_a <= 0) or (side_b <= 0):
            raise ValueError("Sides should be > 0")
        super().__init__()
        self.name = "Rectangle"
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return round(self.side_a * self.side_b, 2)

    @property
    def perimeter(self):
        return round((self.side_a + self.side_b) * 2, 2)
