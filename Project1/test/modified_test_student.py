from person.student import Student
from grade_management.course import Course
import unittest

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class: Initializing resources for TestStudent class.")

    @classmethod
    def tearDownClass(cls):
        print("Teardown Class: Cleaning up resources for TestStudent class.")

    def setUp(self):
        self.name = "Bob"
        self.gender = "Female"
        self.student_id = "S001"
        self.student = Student(self.name, self.gender, self.student_id)

    def tearDown(self):
        print("Teardown: Clean up after a test case.")

    def test_student_initialization(self):
        self.assertEqual(self.student.name, self.name, "Name should match the initialized value.")
        self.assertEqual(self.student.gender, self.gender, "Gender should match the initialized value.")
        self.assertEqual(self.student.student_id, self.student_id, "Student ID should match the initialized value.")
        self.assertIsInstance(self.student, Student, "Object should be an instance of Student.")

    def test_student_enrollment(self):
        course = Course("Math 101", "M101")
        self.student.enroll_course(course)
        self.assertIn(course, self.student.courses, "The course should be added to the student's course list.")
        self.assertEqual(len(self.student.courses), 1, "Student should be enrolled in exactly one course.")
        self.assertEqual(str(self.student.courses[0]), str(course), "The course details should match the enrolled course.")

if __name__ == '__main__':
    unittest.main()
