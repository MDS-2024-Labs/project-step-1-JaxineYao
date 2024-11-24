from person.person import Person

class Student(Person):
    def __init__(self, name="Unknown", gender="Unknown", student_id=None):
        super().__init__(name, gender)
        self.student_id = student_id
        self.courses = []  # 存储学生已注册的课程

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Gender: {self.gender}"

    def enroll_course(self, course):
        """注册课程"""
        self.courses.append(course)

    def list_courses(self):
        """列出学生注册的所有课程"""
        return [str(course) for course in self.courses]