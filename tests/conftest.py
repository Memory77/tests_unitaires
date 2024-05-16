import pytest
import source.shapes as shapes

#factory ficture

@pytest.fixture
def rectangle_factory():
    def create_rectangle(length, width):
        return shapes.Rectangle(length=length,width=width)
    return create_rectangle 



#simple ficture

@pytest.fixture
def my_circle():
    return shapes.Circle(10)
