# Project1: Student and Grade Management System

## Description

This project provides a comprehensive system for managing student data, course information, and grade records. It is organized into multiple packages, each handling specific aspects of the application:  
1.`person`: Handles personal information for students and teachers.  
2.`grade_management`: Manages courses and grades.  
3.`data_access_analysis`: Handles data storage, retrieval, and analysis.  
4.Additional Utilities: Includes `encryption` and `menu` functionalists.  

## Directory Structure
Directory Structure
```
Project1/
├── data_access_analysis/       # Handles data access and analysis
│   ├── __init__.py
│   ├── data_access.py          # Manages data storage and retrieval
│   └── data_analysis.py        # Provides analysis tools for grades
│
├── grade_management/           # Manages courses and grades
│   ├── __init__.py
│   ├── course.py               # Defines courses and their attributes
│   └── grade.py                # Manages grades and related operations
│
├── person/                     # Manages personal information
│   ├── __init__.py
│   ├── person.py               # Base class for Person
│   ├── student.py              # Student class, inherits Person
│   └── teacher.py              # Teacher class, inherits Person
│
├── encryption.py               # Handles data encryption and decryption
├── menu.py                     # Implements the main application menu
├── main.py                     # Main entry point for the application
├── README.md                   # Project documentation
└── readme_files/               # Additional resources for the documentation
```
---

## Sub-Packages

### 1. `person`

#### Purpose:
Handles personal information about students, teachers, and general users.

#### Modules:

1. **`person.py`**:
   - **Person**: A base class for creating a person with basic attributes like `name` and `gender`.

2. **`student.py`**:
   - **Student**: Inherits from `Person`. Adds a unique `student_id` and the ability to register for courses.
   - **Methods**:
     - `__str__()`: Returns a string representation of the student.
     - `enroll_course(course)`: Adds a course to the student’s enrolled list.
     - `list_courses()`: Lists all courses a student is enrolled in.

3. **`teacher.py`**:
   - **Teacher**: Inherits from `Person`. Adds a unique `teacher_id` and manages courses.

---

### 2. `grade_management`

#### Purpose:
Manages course information, grade records, and statistical analysis.

#### Modules:

1. **`course.py`**:
   - **Course**: Handles course details like `course_name` and `course_id`.
   - **Methods**:
     - `__str__()`: Returns a string representation of the course.
     - `add_student(student)`: Adds a student to the course.
     - `list_students()`: Lists all students enrolled in the course.

2. **`grade.py`**:
   - **Grade**: Manages grade records for students in specific courses.
   - **Methods**:
     - `add_grade(student_id, course_id, grade_value)`: Records a grade.
     - `get_grades_by_course(course_id)`: Retrieves all grades for a specific course.

3. **`statistics.py`**:
   - **Statistics**: Provides tools to calculate and visualize grade data.
   - **Methods**:
     - `calculate_statistics(grades)`: Calculates `max`, `min`, and `median` from a list of grades.  
     - `plot_distribution(grades)`: Generates a histogram to visualize grade distribution.

---

### 3. `data_access_analysis`

#### Purpose:
  This package provides functionality for managing data storage, retrieval, and analysis. It ensures efficient handling of student, teacher, and grade data while offering tools for extracting meaningful insights through statistical analysis.

#### Modules:

1. **`data_access.py`**:
   - **Data_access**: Provides methods for storing and retrieving data, including student and teacher information.
   - **Methods**:
     - `add_student()`: Adds a new student to the system.
     - `add_teacher()`: Adds a new teacher to the system.
     - `list_all_students()`: Lists all students currently stored in the system.
     - `list_all_teachers()`: Lists all teachers currently stored in the system.
     - `add_course()`: Adds a new course to the system.
     - `add_grade()`: Adds a grade for a student in a specific course.
     - `get_student_by_id(student_id: str)`: Retrieves a student’s details by their ID.
     - `get_course_by_id(course_id: str)`: Retrieves a course’s details by its ID.
     - `import_all_data_from_csv(file_path: str)`: Imports student, teacher, course, and grade data from a CSV file.

2. **`data_analysis.py`**:
   - **Data_analysis**: Offers tools for analyzing grade data, including calculating averages and generating visualizations.
   - **Methods**:
     - `add_grade(student_id, course_id, grade_value)`: Records a grade.
     - `get_grades_by_course(course_id)`: Retrieves all grades for a specific course.
     
---

### 4. `Additional Utilities`

#### Purpose:
  This section provides supporting utilities to enhance the security and user interaction of the application:
	•	encryption.py: Secures sensitive data using encryption.
	•	menu.py: Implements the main menu logic for seamless user interaction.

#### Modules:

1. **`encryption.py`**:
   - **Data_access**: Provides encryption and decryption utilities to secure sensitive data.
   - **Methods**:
     - `encrypt(data: str)`: str: Encrypts a given string and returns the encrypted version.
     - `decrypt(data: str)`: str: Decrypts a previously encrypted string and returns the original version.

2. **`menu.py`**:
   - **Data_analysis**: Implements the main menu logic to interact with different features of the application.
   - **Methods**:
     - `display_menu()`: Displays the main menu options to the user.
     - `process_choice(choice: int)`: Processes the user’s choice and directs them to the corresponding functionality.
     - `exit_program()`: Handles the exit process for the application.

---

## How to Use

### Installation

Clone the repository:

```bash
git clone https://github.com/your-repo/Project1.git
cd Project1
```

Examples

1. Adding and Listing Students
from person.student import Student
```python
student1 = Student(name="Alice", gender="Female", student_id="S1")
student2 = Student(name="Bob", gender="Male", student_id="S2")

print(student1)  # Output: Student ID: S1, Name: Alice, Gender: Female
```
2. Managing Grades
```python
from grade_management.grade import Grade

# Add grades
Grade.add_grade(student_id="S1", course_id="C1", grade_value=85)
Grade.add_grade(student_id="S2", course_id="C1", grade_value=90)

# Retrieve grades
grades = Grade.get_grades_by_course("C1")
print(grades)  # Output: [{'student_id': 'S1', 'course_id': 'C1', 'grade': 85}, ...]
```
3. Data Analysis
```python
from data_access_analysis.data_analysis import DataAnalysis

DataAnalysis.display_average_grade("S1")
```
Testing

To test the functionality of the package, run the test.py file:
```python
python test.py
```
## Version Control

All group members collaborated using Git. The commit history demonstrates equal contributions. The repository includes separate branches for each sub-package, and merge commits track collaboration.