from person.person import Person

class Student(Person):
    def __init__(self, name, gender, student_id):
        super().__init__(name, gender)
        self.student_id = student_id

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Gender: {self.gender}"