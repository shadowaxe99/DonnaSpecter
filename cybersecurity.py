import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class CyberSecurity:
    def __init__(self, user_profile, security_settings):
        self.user_profile = user_profile
        self.security_settings = security_settings

    def hash_password(self, password):
        salt = self.security_settings.get('salt')
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hashed_password

    def encrypt_data(self, data):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return ciphertext, tag, cipher.nonce

    def decrypt_data(self, ciphertext, tag, nonce):
        key = self.security_settings.get('key')
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data

    def secure_cyber(self):
        for key, value in self.user_profile.items():
            if key in self.security_settings.get('sensitive_data'):
                encrypted_value, tag, nonce = self.encrypt_data(value)
                self.user_profile[key] = {'encrypted_value': encrypted_value, 'tag': tag, 'nonce': nonce}

    def unsecure_cyber(self):
        for key, value in self.user_profile.items():
            if key in self.security_settings.get('sensitive_data'):
                decrypted_value = self.decrypt_data(value.get('encrypted_value'), value.get('tag'), value.get('nonce'))
                self.user_profile[key] = decrypted_value