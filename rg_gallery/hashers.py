# custom_hasher.py
from django.contrib.auth.hashers import BasePasswordHasher
import hashlib

class MyCustomHasher(BasePasswordHasher):
    algorithm = 'my_custom_hasher'

    def encode(self, password, salt):
        # Combine password and salt and hash them using SHA-256
        assert password is not None
        assert salt and '$' not in salt
        hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
        return hash

    def verify(self, password, encoded):
        # Verify whether the given password matches the encoded value
        return self.encode(password, '') == encoded

    def safe_summary(self, encoded):
        # Return a summary of the encoded value for logging
        return {
            'algorithm': self.algorithm,
            'hash': encoded,
        }
