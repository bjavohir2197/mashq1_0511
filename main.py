class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, new_area):
        if self.height == 0:
            raise ValueError("Height 0 bo‘lishi mumkin emas.")
        self.width = new_area / self.height


rect = Rectangle(10, 5)
print("Boshlang‘ich maydon:", rect.area)

rect.area = 100
print("Yangi maydon:", rect.area)
print("O‘zgartirilgan width:", rect.width)
print("Height o‘zgarmagan:", rect.height)
