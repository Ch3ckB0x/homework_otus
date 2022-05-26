from homework_1_oop.src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side should be > 0")
        super().__init__()
        self.name = "Square"
        self.side = side

    @property
    def area(self):
        return round(self.side ** 2, 2)

    @property
    def perimeter(self):
        return round(self.side * 4, 2)
