import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(8) # 64 bits
# key = os.urandom(16) # 128 bits
# key = os.urandom(24) # 192 bits

iv = os.urandom(8)
# iv = os.urandom(16)
# iv = os.urandom(24)

cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))

print(f"key: {key} - iv: {iv}")

# text = "Hello World"
text = "A secret message"

encryptor = cipher.encryptor()
ct = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
print(f"ct: {ct}")

decryptor = cipher.decryptor()
cd = decryptor.update(ct) + decryptor.finalize()
print(f"cd: {cd}")