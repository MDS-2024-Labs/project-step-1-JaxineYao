from cryptography.fernet import Fernet

class Encryption:
    # Assuming we have a predefined key for encryption/decryption
    key = Fernet.generate_key()  # Replace with a static key for consistent encryption
    cipher_suite = Fernet(key)

    @staticmethod
    def encrypt(text):
        return Encryption.cipher_suite.encrypt(text.encode()).decode()

    @staticmethod
    def decrypt(text):
        return Encryption.cipher_suite.decrypt(text.encode()).decode()