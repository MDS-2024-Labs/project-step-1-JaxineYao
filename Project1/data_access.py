import csv
from person.student import Student
from person.teacher import Teacher
from grade_management.course import Course
from grade_management.grade import Grade

class DataAccess:
    students_list = []
    teachers_list = []
    courses_list = []
    grades_list = []
    user_credentials = {}  # 用于存储学生和老师的账号信息

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
    def import_user_credentials(file_path):
        """从CSV文件导入用户账号和密码信息"""
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user_id = row['id']
                    name = row['name']
                    password = row['password']
                    role = row['role']

                    # 存储到 user_credentials 字典
                    DataAccess.user_credentials[user_id] = {
                        'name': name,
                        'password': password,
                        'role': role
                    }
            print(f"User credentials imported successfully from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error occurred during import: {e}")

    @staticmethod
    def validate_student(student_id, password):
        """验证学生登录"""
        user = DataAccess.user_credentials.get(student_id)
        if user and user['role'] == 'student' and user['password'] == password:
            return True
        return False

    @staticmethod
    def validate_teacher(teacher_id, password):
        """验证老师登录"""
        user = DataAccess.user_credentials.get(teacher_id)
        if user and user['role'] == 'teacher' and user['password'] == password:
            return True
        return False

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
    def get_student_by_id(student_id):
        """根据学生ID查找学生信息"""
        for student in DataAccess.students_list:
            if student.student_id == student_id:
                print(student)
                return
        print("Student not found.")

    @staticmethod
    def get_grades_by_student_id(student_id):
        """根据学生ID查找学生成绩"""
        found = False
        for grade in DataAccess.grades_list:
            if grade.student_id == student_id:
                print(grade)
                found = True
        if not found:
            print("No grades found for the student.")

    @staticmethod
    def get_teacher_by_id(teacher_id):
        """根据老师ID查找老师信息"""
        for teacher in DataAccess.teachers_list:
            if teacher.teacher_id == teacher_id:
                print(teacher)
                return
        print("Teacher not found.")

    @staticmethod
    def get_course_by_id(course_id):
        """根据课程ID查找课程信息"""
        for course in DataAccess.courses_list:
            if course.course_id == course_id:
                print(course)
                return
        print("Course not found.")

    @staticmethod
    def import_all_data_from_csv(file_path):
        """从单个CSV文件导入学生、课程和成绩数据"""
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = row.get('student_id')
                    name = row.get('name')
                    gender = row.get('gender')
                    course_id = row.get('course_id')
                    course_name = row.get('course_name', 'Unknown')
                    grade_value = row.get('grade')
                    teacher_name = row.get('teacher_name')

                    # 添加Student对象
                    student = next((s for s in DataAccess.students_list if s.student_id == student_id), None)
                    if not student and student_id and name and gender:
                        student = Student(name, gender, student_id)
                        DataAccess.students_list.append(student)
                        print(f"Student added: {student}")

                    # 添加Course对象
                    course = next((c for c in DataAccess.courses_list if c.course_id == course_id), None)
                    if not course and course_id:
                        course = Course(course_id=course_id, course_name=course_name)
                        DataAccess.courses_list.append(course)
                        print(f"Course added: {course}")

                    # 添加Grade对象
                    if grade_value and course_id and student_id:
                        grade = Grade(student_id=student_id, course_id=course_id, grade=float(grade_value))
                        DataAccess.grades_list.append(grade)
                        print(f"Grade added for student {student_id} in course {course_id}.")

            print("All data imported successfully.")
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error occurred during import: {e}")