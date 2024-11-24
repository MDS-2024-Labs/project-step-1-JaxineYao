import pandas as pd
import matplotlib.pyplot as plt
from data_access_analysis.data_access import DataAccess  
from grade_management.grade import Grade

class DataAnalysis:
    @staticmethod
    def display_average_grade(student_id):
        grades = [g.grade_value for g in DataAccess.grades_list if g.student_id == student_id]
        if grades:
            average_grade = sum(grades) / len(grades)
            print(f"Average grade for Student ID {student_id}: {average_grade:.2f}")
        else:
            print(f"No grades found for Student ID {student_id}.")

    @staticmethod
    def convert_grades_to_gpa(student_id):
        grades = [g.grade_value for g in DataAccess.grades_list if g.student_id == student_id]
        if grades:
            # GPA conversion logic
            def grade_to_gpa(grade):
                if grade >= 90:
                    return 4.0
                elif grade >= 80:
                    return 3.0
                elif grade >= 70:
                    return 2.0
                elif grade >= 60:
                    return 1.0
                else:
                    return 0.0

            gpa = sum(grade_to_gpa(grade) for grade in grades) / len(grades)
            print(f"GPA for Student ID {student_id}: {gpa:.2f}")
        else:
            print(f"No grades found for Student ID {student_id}.")
