from student import Student
from teacher import Teacher
from course import Course
from grade import Grade

class DataAccess:
    students_list = []
    teachers_list = []
    courses_list = []
    grades_list = []

    @staticmethod
    def add_student():
        while True:
            try:
                student_id = input("Input student ID (or '-1' to end): ")
                if student_id == "-1":
                    break
                name = input("Input student name: ")
                gender = input("Input student gender (M/F): ")
                student = Student(name, gender, student_id)
                DataAccess.students_list.append(student)
                print("Student added successfully!")
            except ValueError:
                print("Please input valid data.")

    @staticmethod
    def add_teacher():
        while True:
            try:
                teacher_id = input("Input teacher ID (or '-1' to end): ")
                if teacher_id == "-1":
                    break
                name = input("Input teacher name: ")
                gender = input("Input teacher gender (M/F): ")
                login_name = input("Input teacher login name: ")
                password = input("Input teacher password: ")
                teacher = Teacher(name, gender, teacher_id, login_name, password)
                DataAccess.teachers_list.append(teacher)
                print("Teacher added successfully!")
            except ValueError:
                print("Please input valid data.")

    @staticmethod
    def add_course():
        while True:
            try:
                course_id = input("Input course ID (or '-1' to end): ")
                if course_id == "-1":
                    break
                course_name = input("Input course name: ")
                course = Course(course_name, course_id)
                DataAccess.courses_list.append(course)
                print("Course added successfully!")
            except ValueError:
                print("Please input valid data.")

    @staticmethod
    def add_grade():
        while True:
            try:
                student_id = input("Enter Student ID: ")
                course_id = input("Enter Course ID: ")
                grade_value = float(input("Enter Grade Value: "))
                grade = Grade(student_id, course_id, grade_value)
                DataAccess.grades_list.append(grade)
                print("Grade added successfully!")
            except ValueError:
                print("Please input valid data.")


    @staticmethod
    def list_all_students():
        if not DataAccess.students_list:
            print("No students found.")
        else:
            for student in DataAccess.students_list:
                print(student)

    @staticmethod
    def list_all_teachers():
        if not DataAccess.teachers_list:
            print("No teachers found.")
        else:
            for teacher in DataAccess.teachers_list:
                print(teacher)

    @staticmethod
    def list_all_courses():
        if not DataAccess.courses_list:
            print("No courses found.")
        else:
            for course in DataAccess.courses_list:
                print(course)

    @staticmethod
    def list_all_grades():
        if not DataAccess.grades_list:
            print("No grades found.")
        else:
            for grade in DataAccess.grades_list:
                print(grade)

    @staticmethod
    def get_student_by_id():
        student_id = input("Input student ID for search: ")
        for student in DataAccess.students_list:
            if student.student_id == student_id:
                print(student)
                return
        print("Student not found.")

    @staticmethod
    def get_teacher_by_id():
        teacher_id = input("Input teacher ID for search: ")
        for teacher in DataAccess.teachers_list:
            if teacher.teacher_id == teacher_id:
                print(teacher)
                return
        print("Teacher not found.")

    @staticmethod
    def get_course_by_id():
        course_id = input("Input course ID for search: ")
        for course in DataAccess.courses_list:
            if course.course_id == course_id:
                print(course)
                return
        print("Course not found.")


    @staticmethod
    def get_grade_by_id():
        course_id = input("Input course ID for search: ")
        student_id = input("Input student ID for search: ")
        
        # 查找特定课程和学生的成绩
        for grade in DataAccess.grades_list:
            print(f"Checking Grade: {grade}")
            if grade.course_id == course_id and grade.student_id == student_id:
                print("Found Grade:", grade)
                print(f"Calling get_statistics with course_id: {course_id}")
                # 调用统计方法，传入 DataAccess.grades_list 和 course_id
                Grade.get_statistics(DataAccess.grades_list, course_id)
                return
        
        # 如果没有找到特定学生的成绩
        print("Grade not found.")

