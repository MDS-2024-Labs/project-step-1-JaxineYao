from data_access import DataAccess
from person.person import Person
from person.student import Student
from person.teacher import Teacher

def main_menu():
    print("***** Welcome to the System *****")
    print("1: Student Login")
    print("2: Teacher Login")
    print("0: Exit")

def student_menu(student_id):
    print("***** Student Menu *****")
    print("1: View my information")
    print("2: View my grades")
    print("0: Logout")

    while True:
        choice = input("Please select an option: ")
        if choice == "1":
            DataAccess.get_student_by_id(student_id)
        elif choice == "2":
            DataAccess.get_grades_by_student_id(student_id)
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def teacher_menu():
    print("***** Teacher Menu *****")
    print("1: Add a student")
    print("2: Add a course")
    print("3: Add a teacher")
    print("4: Add a grade")
    print("5: List all students")
    print("6: List all courses")
    print("7: List all teachers")
    print("8: List all grades")
    print("9: Search for a student")
    print("10: Search for a course")
    print("11: Search for a teacher")
    print("12: Search for a grade")
    print("13: Import data from CSV")  # 新增的选项
    print("0: Logout")

    while True:
        choice = input("Please input a number to run the program: ")
        if choice == "1":
            DataAccess.add_student()
        elif choice == "2":
            DataAccess.add_course()
        elif choice == "3":
            DataAccess.add_teacher()
        elif choice == "4":
            DataAccess.add_grade()
        elif choice == "5":
            DataAccess.list_all_students()
        elif choice == "6":
            DataAccess.list_all_courses()
        elif choice == "7":
            DataAccess.list_all_teachers()
        elif choice == "8":
            DataAccess.list_all_grades()
        elif choice == "9":
            student_id = input("Enter student ID: ")
            DataAccess.get_student_by_id(student_id)
        elif choice == "10":
            course_id = input("Enter course ID: ")
            DataAccess.get_course_by_id(course_id)
        elif choice == "11":
            teacher_id = input("Enter teacher ID: ")
            DataAccess.get_teacher_by_id(teacher_id)
        elif choice == "12":
            grade_id = input("Enter grade ID: ")
            DataAccess.get_grade_by_id(grade_id)
        elif choice == "13":  # 导入 CSV 数据选项
            file_path = input("Enter the path to the CSV file: ")
            try:
                DataAccess.import_all_data_from_csv(file_path)
                print(f"Data imported successfully from {file_path}")
            except Exception as e:
                print(f"Failed to import data: {e}")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def login():
    while True:
        main_menu()
        choice = input("Please select an option: ")
        if choice == "1":
            student_id = input("Enter your student ID: ").strip()
            password = input("Enter your password: ").strip()
            if DataAccess.validate_student(student_id, password):
                student_menu(student_id)
            else:
                print("Invalid student ID or password.")
        elif choice == "2":
            teacher_id = input("Enter your teacher ID: ").strip()
            password = input("Enter your password: ").strip()
            if DataAccess.validate_teacher(teacher_id, password):
                teacher_menu()
            else:
                print("Invalid teacher ID or password.")
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    # 导入初始用户数据
    credentials_path = "/Users/orange/project-step-1-JaxineYao/initial_login_data.csv"  # 您的CSV文件路径
    DataAccess.import_user_credentials(credentials_path)
    
    # 启动登录界面
    login()