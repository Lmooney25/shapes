from shapes import shapes_2d
from math import pi


def test_diameter_of_circle():
    radius = 2
    circle = shapes_2d.Circle(radius)

    assert circle.diameter == 4


def test_area_of_circle():
    radius = 2
    circle = shapes_2d.Circle(radius)

    assert circle.area == pi * 4


def test_circumference_of_circle():
    radius = 2
    circle = shapes_2d.Circle(radius)

    assert circle.circumference == 4 * pi
