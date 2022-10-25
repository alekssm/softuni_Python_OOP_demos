import math


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Triangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class ShapesAreaCal:
    def cal_area(self, shape):
        if isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi
        elif isinstance(shape, Rect):
            return shape.a * shape.b

    def cal_area_sum(self, shapes):
        return sum(self.cal_area(x) for x in shapes)


class Printer:
    def print(self, message):
        print(message)


class ShapeController:
    def __init__(self, cal, printer):
        self.cal = cal
        self.printer = printer

    def print_area_sum(self, shapes):
        area_sum = self.cal.cal_area_sum(shapes)
        self.printer.print(f"Area sum is {area_sum}")


shapes = [
    Circle(10),
    Rect(4, 5)
]

ShapeController.print_area_sum(shapes)