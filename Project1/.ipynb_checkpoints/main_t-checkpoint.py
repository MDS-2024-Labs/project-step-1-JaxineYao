def main_menu():
    print("*****  Operation Menu *****")
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
    print("13: Import data from CSV")  
    print("0: Exit the program")

def main():
    main_menu()
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
            DataAccess.get_student_by_id()
        elif choice == "10":
            DataAccess.get_course_by_id()
        elif choice == "11":
            DataAccess.get_teacher_by_id()
        elif choice == "12":
            DataAccess.get_grade_by_id()
        elif choice == "13":
            file_path = input("Enter the path to the CSV file: ")
            DataAccess.import_data_from_csv(file_path)
        elif choice == "0":
            print("Exit succeeded.")
            break
        else:
            print("Sorry, we do not have this function!")
        print("Press any key to continue...")