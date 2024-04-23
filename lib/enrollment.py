from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        """Returns the number of courses the student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """Calculates the average grade for the student across all courses."""
        total_grades = sum(enrollment.grade for enrollment in self._enrollments if enrollment.grade is not None)
        num_courses = sum(1 for enrollment in self._enrollments if enrollment.grade is not None)
        average_grade = total_grades / num_courses if num_courses > 0 else 0
        return average_grade

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def enrollment_count(self):
        """Returns the total number of enrollments for this course."""
        return len(self._enrollments)

class Enrollment:
    all = []

    def __init__(self, student, course, grade=None):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            self.grade = grade
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
