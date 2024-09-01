from cryptography.fernet import Fernet

# load key 
def load_key():
    return open("key.key", "rb").read()

# decrypt
def decrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_name[:-4], "wb") as file:
        file.write(decrypted_data)

# use
key = load_key()
decrypt_file("example.txt.enc", key)
