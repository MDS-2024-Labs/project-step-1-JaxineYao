from person.person import Person
from encryption import Encryption

class Teacher(Person):
    def __init__(self, name, teacher_id, login_name, password):
        super().__init__(name=name, gender=None)  # `gender` 设置为 None，因为它不再需要
        self.teacher_id = teacher_id
        self.login_name = login_name
        self.password = Encryption.encrypt(password)

    def get_password(self, s_key):
        return Encryption.decrypt(self.password) if s_key == "jieyi.yao@student.xjtlu.edu.cn" else "Incorrect key"

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Login: {self.login_name}"