import pytest 
import source.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area",
                          [(3,9), (4,16), (5,25)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area