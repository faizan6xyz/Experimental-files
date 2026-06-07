from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
# Generate keys
private_key = rsa.generate_private_key(
    public_exponent=65537,     # its a methematical parameter used in RSA , 65537 is commonly used because: Secure , Efficient
    key_size=2048   # size of the key , more the size more its secure 
)
public_key = private_key.public_key()
# Encrypt
message = b"Top Secret"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(                # OAEP padding (Optimal Asymmetric Encryption Padding)
        mgf=padding.MGF1(algorithm=hashes.SHA256()),    # MGF (Mask Generation Function)
        algorithm=hashes.SHA256(),     # hashing function 
        label=None     # extra optional data to be attached to the encryption 
    )
)
# Decrypt
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(plaintext)