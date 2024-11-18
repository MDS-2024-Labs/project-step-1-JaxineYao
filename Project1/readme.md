# Project1: Student and Grade Management System

## Description

This project is designed to manage student and course data, along with grade records. It consists of two sub-packages: `person` and `grade_management`. The `person` package manages information about students, teachers, and general user data, while the `grade_management` package handles courses, grade records, and statistical analysis.

## Directory Structure
Directory Structure
```
Project1/
├── person/                    # Sub-package 1: Manages personal information
│   ├── init.py
│   ├── person.py
│   ├── student.py
│   └── teacher.py
│
├── grade_management/          # Sub-package 2: Handles courses and grades
│   ├── init.py
│   ├── course.py
│   ├── grade.py
│   └── statistics.py
│
├── main.py                    # Main entry point for the application
├── test.py                    # Test file demonstrating the package functionality
├── README.md                  # Documentation file
└── .gitignore                 # Ignore unnecessary files
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
3. Calculating Statistics
```python
from grade_management.statistics import Statistics

grades = [{"grade": 85}, {"grade": 90}, {"grade": 78}]
stats = Statistics.calculate_statistics(grades)
print(stats)  # Output: {'max': 90, 'min': 78, 'median': 85}
```
Testing

To test the functionality of the package, run the test.py file:
```python
python test.py
```
## Version Control

All group members collaborated using Git. The commit history demonstrates equal contributions. The repository includes separate branches for each sub-package, and merge commits track collaboration.