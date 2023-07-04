```python
import os
from cryptography.fernet import Fernet

class PrivacyProtection:
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        encoded_text = data.encode()
        cipher_text = self.cipher_suite.encrypt(encoded_text)
        return cipher_text

    def decrypt_data(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def protect_user_profile(self, user_profile):
        encrypted_profile = {key: self.encrypt_data(value) for key, value in user_profile.items()}
        return encrypted_profile

    def unprotect_user_profile(self, encrypted_profile):
        decrypted_profile = {key: self.decrypt_data(value) for key, value in encrypted_profile.items()}
        return decrypted_profile
```
This Python code creates a class `PrivacyProtection` that uses symmetric encryption to protect user data. The encryption key is stored as an environment variable for security. The `encrypt_data` and `decrypt_data` methods are used to encrypt and decrypt data respectively. The `protect_user_profile` and `unprotect_user_profile` methods are used to encrypt and decrypt the user profile data.