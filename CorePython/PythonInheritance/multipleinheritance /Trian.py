class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area_triangle(self):
        area = (0.5) * self.base * self.height
        return area
