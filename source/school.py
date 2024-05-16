class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return f"Student(student_id={self.student_id}, name='{self.name}')"

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def student_count(self):
        return len(self.students)

    def __repr__(self):
        return f"Course(course_id={self.course_id}, title='{self.title}', students={self.students})"