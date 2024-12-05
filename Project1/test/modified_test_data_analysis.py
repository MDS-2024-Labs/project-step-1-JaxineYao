from data_access_analysis.data_analysis import DataAnalysis
from data_access_analysis.data_access import DataAccess
from grade_management.grade import Grade
from person.student import Student
import unittest
from unittest.mock import patch  # For mocking output


class TestDataAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize resources for the TestDataAnalysis class (executed once before all tests)."""
        print("Setup Class: Initializing resources for TestDataAnalysis class.")
        cls.student = Student("Alice", "Female", "S001")
        cls.grade1 = Grade("S001", "M101", 95)
        cls.grade2 = Grade("S001", "CS101", 85)

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after all tests in the TestDataAnalysis class."""
        print("Teardown Class: Cleaning up resources for TestDataAnalysis class.")
        DataAccess.grades_list.clear()

    def setUp(self):
        """Prepare the test environment before each test."""
        DataAccess.students_list.append(self.student)
        DataAccess.grades_list.append(self.grade1)
        DataAccess.grades_list.append(self.grade2)

    def tearDown(self):
        """Clean up the test environment after each test."""
        DataAccess.students_list.clear()
        DataAccess.grades_list.clear()

    @patch('builtins.print')  # Mock the print function
    def test_display_average_grade(self, mock_print):
        """Test the display_average_grade method."""
        # Calculate the expected average grade
        expected_average = (self.grade1.grade_value + self.grade2.grade_value) / 2
        # Call the method to be tested
        DataAnalysis.display_average_grade("S001")
        # Verify the print function is called with the expected output
        mock_print.assert_called_with(f"Average grade for Student ID S001: {expected_average:.2f}")

    @patch('builtins.print')  # Mock the print function
    def test_convert_grades_to_gpa(self, mock_print):
        """Test the convert_grades_to_gpa method."""
        # Call the method to be tested
        DataAnalysis.convert_grades_to_gpa("S001")
        # Verify the print function contains the expected GPA output
        mock_print.assert_any_call("GPA for Student ID S001: 3.50")

if __name__ == '__main__':
    unittest.main()