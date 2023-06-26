import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# key = os.urandom(32) # 256 bits
key = os.urandom(24) # 192 bits
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
# cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

# key = os.urandom(16) # 128 bits
# cipher = Cipher(algorithms.AES128(key), modes.CTR(iv))

# key = os.urandom(32) # 256 bits
# cipher = Cipher(algorithms.AES256(key), modes.CTR(iv))

print(f"key: {key} - iv: {iv}")

# text = "Hello World"
text = "A secret message"

encryptor = cipher.encryptor()
ct = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
print(f"ct: {ct}")

decryptor = cipher.decryptor()
cd = decryptor.update(ct) + decryptor.finalize()
print(f"cd: {cd}")