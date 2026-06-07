import os
import hashlib
import binascii

def hash_password(password: str):
    salt = os.urandom(16)  # random salt
    key = hashlib.pbkdf2_hmac(
        'sha256',                # hash algorithm
        password.encode(),      # password
        salt,                   # salt
        100000                  # iterations (high = secure) , it repeats hashing 100000 times 
    )
    return salt + key  # store both

def verify_password(stored, password):
    salt = stored[:16]
    stored_key = stored[16:]
    
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return new_key == stored_key

# Example
stored = hash_password("my_secure_password")
print(verify_password(stored, "my_secure_password"))