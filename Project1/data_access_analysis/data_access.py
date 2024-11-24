import csv
import pandas as pd
import matplotlib.pyplot as plt
from person.student import Student
from person.teacher import Teacher
from grade_management.course import Course
from grade_management.grade import Grade
from encryption import Encryption

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

                # 检查是否已有相同 student_id 的学生
                existing_student = next((s for s in DataAccess.students_list if s.student_id == student_id), None)

                if existing_student:
                    print(f"Student ID {student_id} already exists.")
                    choice = input("Do you want to overwrite this student? (Y/N): ").strip().lower()

                    if choice == 'y':
                        # 覆盖学生信息
                        existing_student.name = name
                        existing_student.gender = gender
                        print(f"Student with ID {student_id} updated successfully!")
                    elif choice == 'n':
                        # 打印所有现有学生 ID 并重新输入
                        print("Existing Student IDs: ", [s.student_id for s in DataAccess.students_list])
                        print("Please input a new student ID.")
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    # 如果未找到相同的 student_id，添加新学生
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
                login_name = input("Input teacher login name: ")
                password = input("Input teacher password: ")

                # 检查是否已有相同 teacher_id 的老师
                existing_teacher = next((t for t in DataAccess.teachers_list if t.teacher_id == teacher_id), None)

                if existing_teacher:
                    print(f"Teacher ID {teacher_id} already exists.")
                    choice = input("Do you want to overwrite this teacher? (Y/N): ").strip().lower()

                    if choice == 'y':
                        # 覆盖老师信息
                        existing_teacher.name = name
                        existing_teacher.login_name = login_name
                        existing_teacher.password = password
                        print(f"Teacher with ID {teacher_id} updated successfully!")
                    elif choice == 'n':
                        print("Existing Teacher IDs: ", [t.teacher_id for t in DataAccess.teachers_list])
                        print("Please input a new teacher ID.")
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    # 如果未找到相同的 teacher_id，添加新老师
                    teacher = Teacher(name=name, teacher_id=teacher_id, login_name=login_name, password=password)
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
                    user_id = row['ID']
                    name = row['Name']
                    password = str(row['Password'])
                    role = row['Role']

                    # Encrypt the password before storing it
                    encrypted_password = Encryption.encrypt(password)

                    # 存储到 user_credentials 字典
                    DataAccess.user_credentials[user_id] = {
                        'name': name,
                        'password': encrypted_password,
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
        if user and user['role'] == 'Student':
            password = str(password)
            decrypted_password = Encryption.decrypt(user['password'])
            print(f"[DEBUG] Student Validation - Input ID: {student_id}, Input Password: {password}")
            print(f"[DEBUG] Retrieved User: {user}, Decrypted Password: {decrypted_password}")
            return decrypted_password == password
        print(f"[DEBUG] Student Login - User not found or incorrect role: {student_id}")
        return False

    @staticmethod
    def validate_teacher(teacher_id, password):
        """验证老师登录"""
        user = DataAccess.user_credentials.get(teacher_id)
        if user and user['role'] == 'Teacher':
            password = str(password)
            decrypted_password = Encryption.decrypt(user['password'])
            print(f"[DEBUG] Teacher Login - Input Password: {password}, Decrypted Password: {decrypted_password}")
            print(f"[DEBUG] Retrieved User: {user}, Decrypted Password: {decrypted_password}")
            return decrypted_password == password
        print(f"[DEBUG] Teacher Login - User not found or incorrect role: {teacher_id}")
        return False

    @staticmethod
    def add_course():
        while True:
            try:
                course_id = input("Input course ID (or '-1' to end): ")
                if course_id == "-1":
                    break
                course_name = input("Input course name: ")

                # 检查是否已有相同 course_id 的课程
                existing_course = next((c for c in DataAccess.courses_list if c.course_id == course_id), None)

                if existing_course:
                    print(f"Course ID {course_id} already exists.")
                    choice = input("Do you want to overwrite this course? (Y/N): ").strip().lower()

                    if choice == 'y':
                        # 覆盖课程信息
                        existing_course.course_name = course_name
                        print(f"Course with ID {course_id} updated successfully!")
                    elif choice == 'n':
                        print("Existing Course IDs: ", [c.course_id for c in DataAccess.courses_list])
                        print("Please input a new course ID.")
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    # 如果未找到相同的 course_id，添加新课程
                    course = Course(course_name, course_id)
                    DataAccess.courses_list.append(course)
                    print("Course added successfully!")
            except ValueError:
                print("Please input valid data.")

    @staticmethod
    def add_grade():
        while True:
            try:
                student_id = input("Enter Student ID (or '-1' to end): ")
                if student_id == "-1":
                    break
                course_id = input("Enter Course ID: ")
                grade_value = float(input("Enter Grade Value: "))

                # 检查是否已有相同 student_id 和 course_id 的成绩
                existing_grade = next(
                    (g for g in DataAccess.grades_list if g.student_id == student_id and g.course_id == course_id),
                    None
                )

                if existing_grade:
                    print(f"Grade for Student ID {student_id} in Course ID {course_id} already exists.")
                    choice = input("Do you want to overwrite this grade? (Y/N): ").strip().lower()

                    if choice == 'y':
                        # 覆盖成绩信息
                        existing_grade.grade_value = grade_value
                        print(f"Grade for Student ID {student_id} in Course ID {course_id} updated successfully!")
                    elif choice == 'n':
                        print("Existing Grades: ", [
                            (g.student_id, g.course_id) for g in DataAccess.grades_list
                        ])
                        print("Please input a new combination of Student ID and Course ID.")
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    # 如果未找到相同的 student_id 和 course_id，添加新成绩
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
    def get_grade_by_student_and_course(student_id, course_id):
        """根据学生ID和课程ID查找特定成绩"""
        for grade in DataAccess.grades_list:
            if grade.student_id == student_id and grade.course_id == course_id:
                print(f"Grade found: {grade}")
                return
        print("No grade found for the given student ID and course ID.")


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
    def get_grades_by_student_id(student_id):
        """根据学生ID查找学生的所有成绩"""
        found = False
        for grade in DataAccess.grades_list:
            if grade.student_id == student_id:
                print(grade)
                found = True
        if not found:
            print(f"No grades found for the student with ID: {student_id}.")

    @staticmethod
    def import_all_data_from_csv(file_path):
        """从单个CSV文件导入学生、课程和成绩数据，并关联到现有列表"""
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # 提取数据
                    student_id = row.get('Student_ID')
                    student_name = row.get('Student_Name', None)  # 默认值改为 None
                    student_gender = row.get('Gender', 'Unknown')
                    course_id = row.get('Course_ID')
                    course_name = row.get('Course_Name', 'Unknown')
                    grade_value = row.get('Grade_Value')
                    teacher_id = row.get('Teacher_ID')
                    teacher_name = row.get('Teacher_Name', None)  # 默认值改为 None

                    # 添加学生
                    if student_id and not any(s.student_id == student_id for s in DataAccess.students_list):
                        student = Student(name=student_name or "Unnamed Student", gender=student_gender, student_id=student_id)
                        DataAccess.students_list.append(student)
                        print(f"[DEBUG] Added Student: {student}")

                    # 添加老师
                    if teacher_id and not any(t.teacher_id == teacher_id for t in DataAccess.teachers_list):
                        if teacher_name is None:  # 如果 teacher_name 为 None，设置默认名称
                            teacher_name = f"Teacher_{teacher_id}"

                        teacher = Teacher(
                            name=teacher_name,  # 确保传递的 name 不为 None
                            teacher_id=teacher_id,
                            login_name=teacher_id,
                            password="default_password"  # 默认密码
                        )
                        DataAccess.teachers_list.append(teacher)
                        print(f"[DEBUG] Added Teacher: {teacher}")

                    # 添加课程
                    if course_id and not any(c.course_id == course_id for c in DataAccess.courses_list):
                        course = Course(course_name=course_name, course_id=course_id)
                        DataAccess.courses_list.append(course)
                        print(f"[DEBUG] Added Course: {course}")

                    # 添加成绩
                    if grade_value and student_id and course_id:
                        if not any(
                            g.student_id == student_id and g.course_id == course_id
                            for g in DataAccess.grades_list
                        ):
                            grade = Grade(student_id=student_id, course_id=course_id, grade_value=float(grade_value))
                            DataAccess.grades_list.append(grade)
                            print(f"[DEBUG] Added Grade: {grade}")
                
                print(f"Data imported successfully from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error occurred during import: {e}")
            
    @staticmethod
    def get_statistics(course_id):
        for grade in DataAccess.grades_list:
            print(f"Student ID: {grade.student_id}, Course ID: {grade.course_id}, Grade: {grade.grade_value}")
        """计算并展示特定课程的成绩统计信息"""
        grades = [g.grade_value for g in DataAccess.grades_list if g.course_id.strip() == course_id.strip()]
        if not grades:
            print(f"No grades available for Course ID {course_id}.")
            return

        df_grades = pd.DataFrame(grades, columns=["grade_value"])
        median_grade = df_grades["grade_value"].median()
        max_grade = df_grades["grade_value"].max()
        min_grade = df_grades["grade_value"].min()

        print(f"\nStatistics for Course ID {course_id}:")
        print(f"Median: {median_grade}")
        print(f"Max: {max_grade}")
        print(f"Min: {min_grade}")

        plt.figure(figsize=(6, 4))
        plt.boxplot(df_grades["grade_value"], vert=False)
        plt.title(f"Boxplot of Grades for Course ID {course_id}")
        plt.xlabel("Grade Value")
        plt.show()

    @staticmethod
    def get_grade_and_statistics(student_id, course_id):
        print(f"Searching for Student ID: '{student_id}' and Course ID: '{course_id}'")
        print("Current grades_list content:")
        for g in DataAccess.grades_list:
            print(f"Stored: Student ID: '{g.student_id}', Course ID: '{g.course_id}', Grade: {g.grade_value}")
        
        # 在这里筛选
        found_grade = next(
            (g for g in DataAccess.grades_list if g.student_id.strip() == student_id.strip() and g.course_id.strip() == course_id.strip()),
            None
        )

        if found_grade:
            print(f"Found Grade: Student ID {found_grade.student_id}, Course ID {found_grade.course_id}, Grade {found_grade.grade_value}")
            DataAccess.get_statistics(course_id)
        else:
            print(f"No grade found for Student ID: {student_id} and Course ID: {course_id}.")