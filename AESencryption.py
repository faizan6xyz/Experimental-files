from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt(data: bytes, key: bytes):    # this take the data and key in bytes 
    aesgcm = AESGCM(key)   # initialize the encryption engine using the key 
    nonce = os.urandom(12)  # required size for GCM , its a NONCE (number used once ) , here its 12 bits
    ciphertext = aesgcm.encrypt(nonce, data, None) # none is the optional extra data called AAD (Additional Authenticated Data ) its the extra data auhtenticate, this line gives the encryption data + authentication tag as result 
    return nonce + ciphertext
def decrypt(enc_data: bytes, key: bytes):
    nonce = enc_data[:12]
    ciphertext = enc_data[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)

# Example
key = AESGCM.generate_key(bit_length=256)
encrypted = encrypt(b"Secret Message", key)
print(decrypt(encrypted, key))