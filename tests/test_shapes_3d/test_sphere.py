from shapes import shapes_3d
from math import pi


def test_surface_area_of_sphere():
    radius = 2
    sphere = shapes_3d.Sphere(radius)

    assert sphere.surface_area == 16 * pi


def test_volume_of_sphere():
    radius = 2
    sphere = shapes_3d.Sphere(radius)

    assert sphere.volume == (32 / 3) * pi
