from cryptography.fernet import Fernet

# load key
def load_key():
    return open("key.key", "rb").read()

# encryot
def encrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_name + ".enc", "wb") as file:
        file.write(encrypted_data)

# load key
key = load_key()
encrypt_file("example.txt", key)
