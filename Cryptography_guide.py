"""
================================================================================
  PYTHON CRYPTOGRAPHY — COMPLETE ADVANCED REFERENCE
  Covers: Hashing, Symmetric Encryption, Asymmetric Encryption, Digital
          Signatures, Key Derivation, MAC, JWT, TLS, Secrets, Fernet
  Library: cryptography, hashlib, hmac, secrets, jwt
  Install: pip install cryptography pyjwt
================================================================================
"""

import hashlib
import hmac
import secrets
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization, padding as asym_padding
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding as rsa_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hmac as crypto_hmac
from cryptography.hazmat.backends import default_backend


# ============================================================
# 1. HASHING — one-way, no key
# ============================================================
def hashing():
    print("\n--- 1. HASHING ---")

    data = b"Hello Faizan"

    # MD5 (fast, NOT secure for passwords or signatures)
    print("MD5    :", hashlib.md5(data).hexdigest())

    # SHA-1 (deprecated, avoid)
    print("SHA1   :", hashlib.sha1(data).hexdigest())

    # SHA-256 (recommended general purpose)
    print("SHA256 :", hashlib.sha256(data).hexdigest())

    # SHA-512
    print("SHA512 :", hashlib.sha512(data).hexdigest())

    # SHA-3
    print("SHA3   :", hashlib.sha3_256(data).hexdigest())

    # BLAKE2 (fast, secure, modern)
    print("BLAKE2b:", hashlib.blake2b(data).hexdigest())
    print("BLAKE2s:", hashlib.blake2s(data).hexdigest())

    # hash a file in chunks (memory efficient)
    def hash_file(filepath):
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    # verify hash (constant time comparison — prevents timing attacks)
    original = hashlib.sha256(data).digest()
    received = hashlib.sha256(data).digest()
    print("Match  :", hmac.compare_digest(original, received))

    # available algorithms
    print("Available:", hashlib.algorithms_guaranteed)


# ============================================================
# 2. PASSWORD HASHING — slow, salted (use for user passwords)
# ============================================================
def password_hashing():
    print("\n--- 2. PASSWORD HASHING ---")

    password = b"mysecretpassword"

    # PBKDF2 — built into hashlib
    salt = os.urandom(16)
    key  = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password,
        salt=salt,
        iterations=260000,      # OWASP recommended minimum
        dklen=32
    )
    print("PBKDF2 hash:", key.hex())

    # verify PBKDF2
    key_check = hashlib.pbkdf2_hmac("sha256", password, salt, 260000, 32)
    print("PBKDF2 match:", hmac.compare_digest(key, key_check))

    # Scrypt — memory-hard (more resistant to GPU attacks)
    salt2 = os.urandom(16)
    kdf = Scrypt(salt=salt2, length=32, n=2**14, r=8, p=1,
                 backend=default_backend())
    key2 = kdf.derive(password)
    print("Scrypt hash:", key2.hex())

    # verify Scrypt
    kdf_verify = Scrypt(salt=salt2, length=32, n=2**14, r=8, p=1,
                        backend=default_backend())
    try:
        kdf_verify.verify(password, key2)
        print("Scrypt match: True")
    except Exception:
        print("Scrypt match: False")

    # store format: salt + hash together
    stored = base64.b64encode(salt + key).decode()
    print("Stored string:", stored)

    # verify stored password
    decoded   = base64.b64decode(stored)
    s, h      = decoded[:16], decoded[16:]
    new_key   = hashlib.pbkdf2_hmac("sha256", password, s, 260000, 32)
    print("Login check:", hmac.compare_digest(h, new_key))


# ============================================================
# 3. HMAC — keyed hash for message authentication
# ============================================================
def hmac_example():
    print("\n--- 3. HMAC ---")

    key     = secrets.token_bytes(32)
    message = b"Transfer $1000 to account 12345"

    # create HMAC
    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    print("HMAC:", mac)

    # verify (always use compare_digest — prevents timing attacks)
    received_mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    print("Valid:", hmac.compare_digest(mac, received_mac))

    # HMAC with cryptography library
    h = crypto_hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(message)
    signature = h.finalize()
    print("Crypto HMAC:", signature.hex())

    # tamper detection demo
    tampered  = b"Transfer $9999 to account 12345"
    bad_mac   = hmac.new(key, tampered, hashlib.sha256).hexdigest()
    print("Tampered match:", hmac.compare_digest(mac, bad_mac))   # False


# ============================================================
# 4. SECRETS — cryptographically secure random
# ============================================================
def secrets_module():
    print("\n--- 4. SECRETS ---")

    # random bytes
    print("Token bytes:", secrets.token_bytes(32).hex())

    # URL-safe token (for password reset links, API keys)
    print("URL token  :", secrets.token_urlsafe(32))

    # hex token
    print("Hex token  :", secrets.token_hex(32))

    # random integer in range
    print("Random int :", secrets.randbelow(100))

    # random choice (e.g. OTP)
    import string
    alphabet = string.digits
    otp = "".join(secrets.choice(alphabet) for _ in range(6))
    print("OTP        :", otp)

    # secure password generator
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(chars) for _ in range(20))
    print("Password   :", password)

    # compare tokens safely
    a = secrets.token_hex(16)
    b = secrets.token_hex(16)
    print("Equal      :", secrets.compare_digest(a, b))


# ============================================================
# 5. FERNET — symmetric encryption (easy, secure, recommended)
# ============================================================
def fernet_encryption():
    print("\n--- 5. FERNET (Symmetric) ---")

    # generate key
    key   = Fernet.generate_key()
    f     = Fernet(key)
    print("Key:", key.decode())

    # encrypt
    message   = b"Top secret message"
    encrypted = f.encrypt(message)
    print("Encrypted:", encrypted)

    # decrypt
    decrypted = f.decrypt(encrypted)
    print("Decrypted:", decrypted.decode())

    # encrypt with TTL (token expires after N seconds)
    import time
    token = f.encrypt(b"time-sensitive data")
    time.sleep(1)
    try:
        data = f.decrypt(token, ttl=10)    # valid for 10 seconds
        print("TTL decrypt:", data)
    except Exception as e:
        print("Expired:", e)

    # derive Fernet key from password
    password  = b"userpassword"
    salt      = os.urandom(16)
    kdf       = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=260000,
        backend=default_backend()
    )
    key2 = base64.urlsafe_b64encode(kdf.derive(password))
    f2   = Fernet(key2)
    enc  = f2.encrypt(b"encrypted with password-derived key")
    print("Password-derived decrypt:", f2.decrypt(enc))

    # multi-key rotation
    key_old   = Fernet.generate_key()
    key_new   = Fernet.generate_key()
    multi_f   = Fernet(key_old)
    token_old = multi_f.encrypt(b"old data")

    # rotate — try new key first, fall back to old
    from cryptography.fernet import MultiFernet
    mf        = MultiFernet([Fernet(key_new), Fernet(key_old)])
    print("Multi decrypt:", mf.decrypt(token_old))
    rotated   = mf.rotate(token_old)   # re-encrypt with new key
    print("Rotated:", mf.decrypt(rotated))


# ============================================================
# 6. AES — low-level symmetric encryption
# ============================================================
def aes_encryption():
    print("\n--- 6. AES ENCRYPTION ---")

    key       = os.urandom(32)        # AES-256
    plaintext = b"Secret data 1234"  # must be 16-byte multiple for CBC

    # --- AES-CBC (needs padding) ---
    iv      = os.urandom(16)
    padder  = asym_padding.PKCS7(128).padder()
    padded  = padder.update(plaintext) + padder.finalize()

    cipher  = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    enc     = cipher.encryptor()
    ct      = enc.update(padded) + enc.finalize()
    print("AES-CBC encrypted:", ct.hex())

    # decrypt CBC
    dec     = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    padded2 = dec.update(ct) + dec.finalize()
    unpadder = asym_padding.PKCS7(128).unpadder()
    pt      = unpadder.update(padded2) + unpadder.finalize()
    print("AES-CBC decrypted:", pt)

    # --- AES-GCM (authenticated — recommended, no padding needed) ---
    key2    = os.urandom(32)
    iv2     = os.urandom(12)           # 96-bit nonce for GCM
    aad     = b"authenticated header"  # additional authenticated data (not encrypted)

    encryptor = Cipher(
        algorithms.AES(key2),
        modes.GCM(iv2),
        backend=default_backend()
    ).encryptor()
    encryptor.authenticate_additional_data(aad)
    ct2     = encryptor.update(plaintext) + encryptor.finalize()
    tag     = encryptor.tag              # authentication tag
    print("AES-GCM encrypted:", ct2.hex())
    print("GCM tag          :", tag.hex())

    # decrypt GCM
    decryptor = Cipher(
        algorithms.AES(key2),
        modes.GCM(iv2, tag),
        backend=default_backend()
    ).decryptor()
    decryptor.authenticate_additional_data(aad)
    pt2 = decryptor.update(ct2) + decryptor.finalize()
    print("AES-GCM decrypted:", pt2)

    # --- AES-CTR (stream mode, no padding) ---
    key3    = os.urandom(32)
    nonce   = os.urandom(16)
    cipher3 = Cipher(algorithms.AES(key3), modes.CTR(nonce), backend=default_backend())
    ct3     = cipher3.encryptor().update(plaintext)
    pt3     = Cipher(algorithms.AES(key3), modes.CTR(nonce), backend=default_backend()).decryptor().update(ct3)
    print("AES-CTR decrypted:", pt3)


# ============================================================
# 7. RSA — asymmetric encryption (public/private key)
# ============================================================
def rsa_encryption():
    print("\n--- 7. RSA ENCRYPTION ---")

    # generate key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # serialize to PEM
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b"keypassword")
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Private PEM:\n", pem_private.decode()[:100], "...")
    print("Public  PEM:\n", pem_public.decode()[:100], "...")

    # save to files
    with open("private.pem", "wb") as f:
        f.write(pem_private)
    with open("public.pem", "wb") as f:
        f.write(pem_public)

    # load from file
    with open("private.pem", "rb") as f:
        loaded_private = serialization.load_pem_private_key(
            f.read(), password=b"keypassword", backend=default_backend()
        )

    # encrypt with public key (only private key can decrypt)
    message   = b"RSA encrypted secret"
    encrypted = public_key.encrypt(
        message,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("RSA encrypted:", encrypted.hex()[:40], "...")

    # decrypt with private key
    decrypted = private_key.decrypt(
        encrypted,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("RSA decrypted:", decrypted)


# ============================================================
# 8. DIGITAL SIGNATURES — RSA & ECDSA
# ============================================================
def digital_signatures():
    print("\n--- 8. DIGITAL SIGNATURES ---")

    message = b"Sign this document"

    # --- RSA Signature ---
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # sign
    signature = private_key.sign(
        message,
        rsa_padding.PSS(
            mgf=rsa_padding.MGF1(hashes.SHA256()),
            salt_length=rsa_padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("RSA signature:", signature.hex()[:40], "...")

    # verify
    try:
        public_key.verify(
            signature,
            message,
            rsa_padding.PSS(
                mgf=rsa_padding.MGF1(hashes.SHA256()),
                salt_length=rsa_padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("RSA signature: VALID")
    except Exception:
        print("RSA signature: INVALID")

    # --- ECDSA Signature (smaller keys, faster, same security) ---
    ec_private = ec.generate_private_key(ec.SECP256R1(), default_backend())
    ec_public  = ec_private.public_key()

    ec_sig = ec_private.sign(message, ec.ECDSA(hashes.SHA256()))
    print("ECDSA signature:", ec_sig.hex()[:40], "...")

    try:
        ec_public.verify(ec_sig, message, ec.ECDSA(hashes.SHA256()))
        print("ECDSA signature: VALID")
    except Exception:
        print("ECDSA signature: INVALID")

    # tamper detection
    tampered = b"Sign this TAMPERED document"
    try:
        public_key.verify(
            signature,
            tampered,
            rsa_padding.PSS(
                mgf=rsa_padding.MGF1(hashes.SHA256()),
                salt_length=rsa_padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Tampered: VALID")
    except Exception:
        print("Tampered: INVALID — tampering detected")


# ============================================================
# 9. KEY DERIVATION — HKDF, PBKDF2, Scrypt
# ============================================================
def key_derivation():
    print("\n--- 9. KEY DERIVATION ---")

    # HKDF — derive key from existing key material (not passwords)
    input_key = os.urandom(32)
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"encryption key",
        backend=default_backend()
    )
    derived_key = hkdf.derive(input_key)
    print("HKDF derived key:", derived_key.hex())

    # derive multiple keys from one master key
    master = os.urandom(32)

    hkdf_enc = HKDF(algorithm=hashes.SHA256(), length=32, salt=None,
                    info=b"enc", backend=default_backend())
    hkdf_mac = HKDF(algorithm=hashes.SHA256(), length=32, salt=None,
                    info=b"mac", backend=default_backend())

    enc_key = hkdf_enc.derive(master)
    mac_key = hkdf_mac.derive(master)
    print("Enc key:", enc_key.hex()[:20], "...")
    print("MAC key:", mac_key.hex()[:20], "...")

    # PBKDF2 — for passwords
    salt = os.urandom(16)
    kdf  = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=260000,
        backend=default_backend()
    )
    key = kdf.derive(b"user_password")
    print("PBKDF2 key:", key.hex())


# ============================================================
# 10. ENCODING — Base64, Hex
# ============================================================
def encoding():
    print("\n--- 10. ENCODING ---")

    data = b"Binary \x00\x01\x02 data"

    # Base64
    b64     = base64.b64encode(data)
    decoded = base64.b64decode(b64)
    print("Base64 :", b64)
    print("Decoded:", decoded)

    # URL-safe Base64 (safe for URLs and filenames)
    url_b64 = base64.urlsafe_b64encode(data)
    print("URL B64:", url_b64)

    # Hex
    hexed    = data.hex()
    unhexed  = bytes.fromhex(hexed)
    print("Hex    :", hexed)
    print("Unhex  :", unhexed)

    # encode/decode string
    text      = "Hello Faizan"
    b64_str   = base64.b64encode(text.encode()).decode()
    orig_str  = base64.b64decode(b64_str).decode()
    print("B64 str:", b64_str)
    print("Orig   :", orig_str)


# ============================================================
# 11. JWT — JSON Web Tokens
# ============================================================
def jwt_tokens():
    print("\n--- 11. JWT ---")

    try:
        import jwt
        import datetime

        secret = secrets.token_hex(32)

        # create token
        payload = {
            "user_id": 42,
            "name":    "Faizan",
            "role":    "admin",
            "exp":     datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            "iat":     datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, secret, algorithm="HS256")
        print("JWT Token:", token[:40], "...")

        # decode and verify
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        print("Decoded:", decoded)

        # RS256 — asymmetric JWT (production recommended)
        private_key = rsa.generate_private_key(65537, 2048, default_backend())
        public_key  = private_key.public_key()

        pem_priv = private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()
        )
        pem_pub = public_key.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        )

        rs256_token   = jwt.encode(payload, pem_priv, algorithm="RS256")
        rs256_decoded = jwt.decode(rs256_token, pem_pub, algorithms=["RS256"])
        print("RS256 decoded:", rs256_decoded["name"])

        # expired token
        old_payload = {**payload, "exp": datetime.datetime.utcnow() - datetime.timedelta(hours=1)}
        old_token   = jwt.encode(old_payload, secret, algorithm="HS256")
        try:
            jwt.decode(old_token, secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            print("Token expired — caught correctly")

    except ImportError:
        print("pyjwt not installed — run: pip install pyjwt")


# ============================================================
# 12. SECURE FILE ENCRYPTION — full workflow
# ============================================================
def file_encryption():
    print("\n--- 12. FILE ENCRYPTION ---")

    # write a test file
    with open("secret.txt", "wb") as f:
        f.write(b"This is a secret file with sensitive data.")

    # encrypt file with Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open("secret.txt", "rb") as f:
        original = f.read()

    encrypted = fernet.encrypt(original)

    with open("secret.enc", "wb") as f:
        f.write(encrypted)
    print("File encrypted to secret.enc")

    # decrypt file
    with open("secret.enc", "rb") as f:
        enc_data = f.read()

    decrypted = fernet.decrypt(enc_data)

    with open("secret_decrypted.txt", "wb") as f:
        f.write(decrypted)
    print("File decrypted to secret_decrypted.txt")
    print("Content:", decrypted.decode())


# ============================================================
# 13. ENCRYPT-THEN-MAC — manual authenticated encryption
# ============================================================
def encrypt_then_mac():
    print("\n--- 13. ENCRYPT-THEN-MAC ---")

    # derive separate keys for encryption and MAC from one password
    password = b"strongpassword"
    salt     = os.urandom(16)

    master = hashlib.pbkdf2_hmac("sha256", password, salt, 260000, 64)
    enc_key = master[:32]
    mac_key = master[32:]

    # encrypt with AES-CBC
    iv      = os.urandom(16)
    padder  = asym_padding.PKCS7(128).padder()
    message = b"Sensitive data here"
    padded  = padder.update(message) + padder.finalize()
    cipher  = Cipher(algorithms.AES(enc_key), modes.CBC(iv), backend=default_backend())
    ct      = cipher.encryptor().update(padded) + cipher.encryptor().finalize()

    # MAC over salt + iv + ciphertext
    mac = hmac.new(mac_key, salt + iv + ct, hashlib.sha256).digest()

    # package: salt + iv + mac + ciphertext
    package = salt + iv + mac + ct
    print("Package length:", len(package), "bytes")

    # verify and decrypt
    s   = package[:16]
    i   = package[16:32]
    m   = package[32:64]
    c   = package[64:]

    master2  = hashlib.pbkdf2_hmac("sha256", password, s, 260000, 64)
    enc_key2 = master2[:32]
    mac_key2 = master2[32:]

    expected_mac = hmac.new(mac_key2, s + i + c, hashlib.sha256).digest()
    if not hmac.compare_digest(m, expected_mac):
        raise ValueError("MAC verification failed — data tampered")

    dec     = Cipher(algorithms.AES(enc_key2), modes.CBC(i), backend=default_backend()).decryptor()
    padded2 = dec.update(c) + dec.finalize()
    unpad   = asym_padding.PKCS7(128).unpadder()
    plain   = unpad.update(padded2) + unpad.finalize()
    print("Decrypted:", plain)


# ============================================================
# 14. ELLIPTIC CURVE DIFFIE-HELLMAN (ECDH) — key exchange
# ============================================================
def ecdh_key_exchange():
    print("\n--- 14. ECDH KEY EXCHANGE ---")

    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

    # Alice generates her key pair
    alice_private = X25519PrivateKey.generate()
    alice_public  = alice_private.public_key()

    # Bob generates his key pair
    bob_private = X25519PrivateKey.generate()
    bob_public  = bob_private.public_key()

    # Exchange public keys, derive shared secret
    alice_shared = alice_private.exchange(bob_public)
    bob_shared   = bob_private.exchange(alice_public)

    print("Alice shared:", alice_shared.hex())
    print("Bob shared  :", bob_shared.hex())
    print("Match       :", alice_shared == bob_shared)   # True

    # derive final key from shared secret using HKDF
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"session key",
        backend=default_backend()
    )
    session_key = hkdf.derive(alice_shared)
    print("Session key:", session_key.hex())


# ============================================================
# 15. QUICK REFERENCE
# ============================================================
"""
ALGORITHM CHEAT SHEET
=====================

USE CASE                    ALGORITHM           NOTES
---------------------------|-------------------|--------------------------------
Hash (general)             | SHA-256 / SHA-3   | One-way, no key
Hash (fast, modern)        | BLAKE2b            | Faster than SHA, still secure
Password hashing           | Scrypt / PBKDF2   | Slow by design, use salt
Message auth (HMAC)        | HMAC-SHA256        | Keyed hash, tamper detection
Symmetric encryption       | Fernet / AES-GCM  | Same key to enc/dec
Asymmetric encryption      | RSA-OAEP (2048+)  | Public=encrypt, private=decrypt
Digital signature          | RSA-PSS / ECDSA   | Private=sign, public=verify
Key exchange               | X25519 / ECDH     | Agree on shared secret securely
Key derivation (password)  | PBKDF2 / Scrypt   | Stretch weak password to key
Key derivation (key mat.)  | HKDF              | Derive keys from existing keys
Tokens (auth, API keys)    | secrets module    | Use token_urlsafe()
JWT                        | HS256 / RS256     | HS256=shared, RS256=asymmetric

GOLDEN RULES
============
1. NEVER roll your own crypto — use established libraries
2. NEVER reuse nonces/IVs with the same key
3. ALWAYS use constant-time comparison (hmac.compare_digest)
4. ALWAYS use authenticated encryption (AES-GCM or Fernet)
5. NEVER store plaintext passwords — always hash with Scrypt/PBKDF2
6. ALWAYS use os.urandom() for random bytes, never random module
7. Prefer Fernet over raw AES for simplicity and safety
8. Use 2048+ bit RSA or ECDSA P-256 for asymmetric crypto
"""


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    hashing()
    password_hashing()
    hmac_example()
    secrets_module()
    fernet_encryption()
    aes_encryption()
    rsa_encryption()
    digital_signatures()
    key_derivation()
    encoding()
    jwt_tokens()
    file_encryption()
    encrypt_then_mac()
    ecdh_key_exchange()

    print("\nDone.")