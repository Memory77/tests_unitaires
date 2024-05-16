import source.shapes as shapes
import pytest 



# les fixtures sont dans conftest


def test_area(rectangle_factory):
    rectangle = rectangle_factory(10, 20)
    assert rectangle.area() == 10 * 20

def test_perimeter(rectangle_factory):
    rectangle = rectangle_factory(10, 20)
    assert rectangle.perimeter() == 10*2 + 20*2

def test_eq(rectangle_factory):
    rectangle = rectangle_factory(10, 20)
    another_rectangle = rectangle_factory(10, 20)
    assert rectangle == another_rectangle