from data_access_analysis.data_analysis import DataAnalysis
from data_access_analysis.data_access import DataAccess
from grade_management.grade import Grade
from person.student import Student
import unittest

class TestDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class: Initializing resources for TestDataAnalysis class.")
        cls.student = Student("Alice", "Female", "S001")
        cls.grade1 = Grade("S001", "M101", 95)
        cls.grade2 = Grade("S001", "CS101", 85)

    @classmethod
    def tearDownClass(cls):
        print("Teardown Class: Cleaning up resources for TestDataAnalysis class.")
        DataAccess.grades_list.clear()

    def setUp(self):
        DataAccess.students_list.append(self.student)
        DataAccess.grades_list.append(self.grade1)
        DataAccess.grades_list.append(self.grade2)

    def tearDown(self):
        DataAccess.students_list.clear()
        DataAccess.grades_list.clear()

    def test_display_average_grade(self):
        expected_average = (self.grade1.grade_value + self.grade2.grade_value) / 2
        with self.assertLogs(level='INFO') as log:
            DataAnalysis.display_average_grade("S001")
        self.assertIn(f"Average grade for Student ID S001: {expected_average:.2f}", log.output[0])

    def test_convert_grades_to_gpa(self):
        with self.assertLogs(level='INFO') as log:
            DataAnalysis.convert_grades_to_gpa("S001")
        self.assertIn("GPA for Student ID S001: ", log.output[0], "GPA conversion log message should be present.")

if __name__ == '__main__':
    unittest.main()
