class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = "Male" if gender == "M" else "Female"

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}"