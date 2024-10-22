# Треба прописати pip install pycryptodome
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


Key = os.urandom(32)
Iv = os.urandom(16)

#CRT
def EncryptAes256(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data)


def DecryptAes256(enc_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(enc_data) + decryptor.finalize()


InputText = "Hello world !!!!"

print(f"Key = {Key}")
print(f"Iv = {Iv}", end = '\n\n')
InputText = InputText.encode('utf-8')
encrypted = EncryptAes256(InputText, Key, Iv)
print(f"Encrypted = {encrypted}")
decrypted = DecryptAes256(encrypted, Key, Iv)
print(f"Decrypted = {decrypted.decode()}")