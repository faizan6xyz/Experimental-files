from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os
# =========================
# 1. RSA KEY GENERATION
# =========================
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key
# =========================
# 2. AES ENCRYPTION
# =========================
def aes_encrypt(data: bytes, key: bytes):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce + ciphertext
def aes_decrypt(enc_data: bytes, key: bytes):
    nonce = enc_data[:12]
    ciphertext = enc_data[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)
# =========================
# 3. HYBRID ENCRYPTION
# =========================
def hybrid_encrypt(message: str, public_key):
    # Convert message → bytes
    data = message.encode()
    # Step 1: Generate AES key
    aes_key = AESGCM.generate_key(bit_length=256)
    # Step 2: Encrypt data with AES
    encrypted_data = aes_encrypt(data, aes_key)
    # Step 3: Encrypt AES key with RSA
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key, encrypted_data
# =========================
# 4. HYBRID DECRYPTION
# =========================
def hybrid_decrypt(encrypted_key, encrypted_data, private_key):
    # Step 1: Decrypt AES key using RSA
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Step 2: Decrypt data using AES
    decrypted_data = aes_decrypt(encrypted_data, aes_key)
    return decrypted_data.decode()
# =========================
# 5. TEST / MAIN
# =========================
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()
    message = "This is a secret message 🔐"
    print("Original:", message)
    # Encrypt
    encrypted_key, encrypted_data = hybrid_encrypt(message, public_key)
    print("\nEncrypted AES Key:", encrypted_key)
    print("Encrypted Data:", encrypted_data)
    # Decrypt
    decrypted_message = hybrid_decrypt(encrypted_key, encrypted_data, private_key)
    print("\nDecrypted:", decrypted_message)