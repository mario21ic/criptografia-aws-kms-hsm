import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# key = os.urandom(16) # 128 bits
# key = os.urandom(24) # 192 bits
key = os.urandom(32) # 256 bits
nonce = os.urandom(16)
algorithm = algorithms.Camellia(key)
cipher = Cipher(algorithm, modes.CBC(nonce))

print(f"key: {key} - nonce: {nonce}")

# text = "Hello World"
text = "A secret message"

encryptor = cipher.encryptor()
ct = encryptor.update(text.encode('utf-8'))
print(f"ct: {ct}")

decryptor = cipher.decryptor()
cd = decryptor.update(ct)
print(f"cd: {cd}")