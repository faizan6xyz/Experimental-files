from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256 # ECC shared secret is NOT directly usable as an AES key , So we convert it into a proper key using SHA256
# STEP 1: Receiver generates ECC keys
receiver_key = ECC.generate(curve='P-256')
receiver_private = receiver_key
receiver_public = receiver_key.public_key()
# STEP 2: Sender side
# Generate AES key
aes_key = get_random_bytes(16)
# Encrypt message using AES
data = b"Hello, this is secret!"
cipher = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
# Simulate ECC key exchange (shared secret)
shared_secret = receiver_public.pointQ * receiver_private.d
shared_key = SHA256.new(str(shared_secret).encode()).digest()[:16]
# Encrypt AES key using shared key
cipher_key = AES.new(shared_key, AES.MODE_EAX)
encrypted_aes_key, tag2 = cipher_key.encrypt_and_digest(aes_key)
# STEP 3: Receiver side
# Recreate shared key
shared_secret_receiver = receiver_public.pointQ * receiver_private.d
shared_key_receiver = SHA256.new(str(shared_secret_receiver).encode()).digest()[:16]
# Decrypt AES key
cipher_key_dec = AES.new(shared_key_receiver, AES.MODE_EAX, nonce=cipher_key.nonce)
decrypted_aes_key = cipher_key_dec.decrypt(encrypted_aes_key)
# Decrypt message
cipher_dec = AES.new(decrypted_aes_key, AES.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt(ciphertext)
print("Decrypted message:", plaintext.decode())