from cryptography.fernet import Fernet
import os  
'''
key = Fernet.generate_key()
# generate a key and save it 
with open("key.key", "wb") as f:
    f.write(key)
print("Key saved successfully!")
'''
# creating multiple keys leads to keys working error and data undecrption , the data could be decrypted by the key which encrypted it .
# Load key from file , wb is write binary and rb is read binary 
with open("key.key", "rb") as f:
    key = f.read()
cipher = Fernet(key)
# Data to encrypt , data is in bytes if its not we use encode() . because encryption works in bytes not in string
data = b"My secret data"
# Encrypt
encrypted = cipher.encrypt(data)
print("Encrypted:", encrypted)
# Decrypt . after the is decrpypted to convert the data back to string we use decode() and ttl is a time to live - means the token is vaid for that seconds 
decrypted = cipher.decrypt(encrypted , ttl=60)
print("Decrypted:", decrypted.decode())
# check the location of the key 
print(os.getcwd())
'''
#delete all the keys 
if os.path.exists("key.key"):
    os.remove("key.key")
    print("Key deleted successfully!")
else:
    print("No key found.")
'''
   







'''
# Fernet is a high-level encryption system from Python’s cryptography library.
 [ Plain Text → Encrypt → Token → Decrypt → Plain Text ]
  It uses:
1. AES (for encryption) : Advanced Encryption Standard - A symmetric encryption algorithm Used to convert readable data → unreadable data
["data" → (AES) → "8xK#@!2..."]
2. HMAC (for integrity check) : Hash-based Message Authentication Code - Ensures data is not changed , Uses Secret key (A private piece of data used to lock and unlock information) and Hash function (Converts data into a fixed-size random-looking value) and then generates a signature (A proof that data is original and untampered) 
[Data + Secret key → HMAC → signature]
# fernet working process : 
1. Generates random IV (initialization vector)
2. Encrypts data using AES
3. Adds timestamp
4. Creates HMAC signature

# token is the final encrypted output from Fernet
# AES, DES, RSA, ECC, SHA-256, etc. are cyprotgraphic algorithm 
# fernet is not ideal for Multi-user systems , Public-key scenarios

# for Multi-User Encryption Systems ( WhatsApp , Cloud storage , Your app with many users ) : Proper Method is Hybrid Encryption , Combination of AES (symmetric) for fast encryption of data and RSA / ECC (asymmetric)for secure key exchange
[User → generates AES key → Encrypt data using AES → Encrypt AES key using receiver's PUBLIC key (RSA/ECC) → Send both ]
[Receiver: Private key → decrypt AES key and AES key → decrypt data]
# for Public-Key Scenarios (HTTPS , Login systems , APIs , Secure messaging ) : Proper Methods is RSA [ Public key → encrypt and Private key → ecrypt ] or  ECC [ Server → shares PUBLIC key and Client → encrypts data and Server → decrypts using PRIVATE key ]

# types of cryptography : 
1.) Symmetric Key Cryptography
    Symmetric Key Cryptography is an encryption system where the sender and receiver of a message use a single common key to encrypt and decrypt messages.
    Symmetric Key cryptography is faster and simpler but the problem is that the sender and receiver have to somehow exchange keys securely.
    The most popular symmetric key cryptography systems are Data Encryption Systems (DES) and Advanced Encryption Systems (AES) .
2.) In Asymmetric Key :
    Cryptography a pair of keys is used to encrypt and decrypt information. A sender's public key is used for encryption and a receiver's private key is used for decryption. Public keys and Private keys are different. Even if the public key is known by everyone the intended receiver can only decode it because he holds his private key. asymmetric key cryptography algorithm are Rivest-Shamir-Adleman(RSA) and Elliptic Curve Cryptography (ECC) .
3.) Hash Functions :
    Hash functions do not require a key. Instead, they use mathematical algorithms to convert messages of any arbitrary length into a fixed-length output, known as a hash value or digest.
    Hash functions are designed to be one-way, meaning the original input cannot be derived from the output.
    it include SHA-1 , SHA-256 , MD5 , MD6 .
'''

# GCM (Galois/Counter Mode) is a high-performance, symmetric-key block cipher mode providing both confidentiality (encryption) and authenticity (integrity) for data.

# A salt is a random, non-secret string of data added to a password before it is hashed to create a unique, scrambled result.