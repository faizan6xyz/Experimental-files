import bcrypt
# Hash password before storing
password = "mypassword".encode('utf-8')
# A salt is a random, non-secret string of data added to a password before it is hashed to create a unique, scrambled result.
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# Store 'hashed' in DB
print(hashed)
entered = "mypassword".encode('utf-8')
if bcrypt.checkpw(entered, hashed):
    print("Correct password")
else:
    print("Wrong password")