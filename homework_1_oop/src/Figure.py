class Figure:
    def __init__(self):
        self.name = "Figure"

    @property
    def area(self):
        return 0

    @property
    def perimeter(self):
        return 0

    def add_area(self, figure):
        if isinstance(figure, Figure):
            all_area = self.area + figure.area
            return all_area
        else:
            raise ValueError("The object is not a Figure")
