from person.teacher import Teacher

class TestTeacher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class: Initializing resources for TestTeacher class.")

    @classmethod
    def tearDownClass(cls):
        print("Teardown Class: Cleaning up resources for TestTeacher class.")

    def setUp(self):
        self.name = "Dr. Smith"
        self.teacher_id = "T001"
        self.login_name = "drsmith"
        self.password = "securepassword"
        self.teacher = Teacher(self.name, self.teacher_id, self.login_name, self.password)

    def tearDown(self):
        print("Teardown: Clean up after a test case.")

    def test_teacher_initialization(self):
        self.assertEqual(self.teacher.name, self.name, "Name should match the initialized value.")
        self.assertEqual(self.teacher.teacher_id, self.teacher_id, "Teacher ID should match the initialized value.")
        self.assertEqual(self.teacher.login_name, self.login_name, "Login name should match the initialized value.")
        self.assertNotEqual(self.teacher.password, self.password, "Password should be encrypted.")
        self.assertIsInstance(self.teacher, Teacher, "Object should be an instance of Teacher.")

    def test_teacher_password_decryption(self):
        correct_key = "jieyi.yao@student.xjtlu.edu.cn"
        decrypted_password = self.teacher.get_password(correct_key)
        self.assertEqual(decrypted_password, self.password, "Decryption should return the original password.")
        
        wrong_key = "wrong_key"
        self.assertEqual(self.teacher.get_password(wrong_key), "Incorrect key", "Decryption should fail with the wrong key.")

if __name__ == '__main__':
    unittest.main()
