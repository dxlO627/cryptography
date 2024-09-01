from cryptography.fernet import Fernet

# create key and save
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# use
generate_key()
