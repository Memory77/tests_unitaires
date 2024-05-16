import pytest
from source.school import Student, Course

@pytest.fixture
def student_factory():
    def create_student(student_id, name):
        return Student(student_id=student_id, name=name)
    return create_student

@pytest.fixture
def course_factory():
    def create_course(course_id, title):
        return Course(course_id=course_id, title=title)
    return create_course


def test_add_student(student_factory, course_factory):
    student = student_factory(4, "Joe")
    course = course_factory(1, "mathematique")
    course.add_student(student)
    assert student in course.students

def test_add_physics(student_factory, course_factory):
    student_one = student_factory(5, "Pitt")
    student_two = student_factory(5, "Pitt")
    student_list = [student_one, student_two]
    course = course_factory(2, "physics")

    for student in student_list:
        course.add_student(student)

    assert course.student_count() == 2

    for student in student_list:
        assert student in course.students
