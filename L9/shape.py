import math

class Shape:
    def area(self):
        raise NotImplementedError("Metoda area() trebuie implementata in subclase.")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Raza trebuie sa fie pozitiva.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensiunile trebuie sa fie pozitive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

try:
    circle = Circle(5)
    rectangle = Rectangle(10, 4)

    print(circle)
    print(rectangle)

except ValueError as e:
    print("Eroare:", e)
