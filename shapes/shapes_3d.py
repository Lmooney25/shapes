from math import pi


class Sphere:
    def __init__(self, radius: int) -> None:
        self.radius = radius 

    @property
    def surface_area(self) -> float:
        return 4 * pi * self.radius**2

    @property
    def volume(self) -> float:
        return (4 / 3) * pi * self.radius**3


class Couboid:
    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self) -> int:
        return (
            2 * self.length * self.width
            + 2 * self.length * self.height
            + 2 * self.width * self.height
        )

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height


class Cube:
    def __init__(self, length: int) -> None:
        self.length = length

    def surface_area(self) -> int:
        return 6 * self.length

    @property
    def volume(self) -> int:
        return self.length**3
