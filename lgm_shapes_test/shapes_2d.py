from math import pi


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return pi * self.radius**2

    @property
    def circumference(self) -> float:
        return 2 * pi * self.radius

    @property
    def diameter(self) -> int:
        return 2 * self.radius


class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    @property
    def area(self) -> int:
        return self.length * self.width

    @property
    def circumference(self) -> int:
        return 2 * (self.length + self.width)


class Square:
    def __init__(self, length: int) -> None:
        self.length = length

    @property
    def area(self) -> int:
        return self.length**2

    @property
    def circumference(self) -> int:
        return self.length * 4
