#!/usr/bin/env python
# Example: ./keygen_test_encrypt.py my2_pub.pem HelloWorld

import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

file_name = "default"
if len(sys.argv)>= 1:
    file_name = sys.argv[1]
print(f"Key file: {file_name}")

original_text = "HelloWorld"
if len(sys.argv)>= 2:
    original_tex = sys.argv[2]
print(f"Texto to encrypt: {original_text}")

with open(file_name, 'rb') as pem_in:
    public_key = serialization.load_pem_public_key(pem_in.read())


# Cifrar un mensaje
#original_text = b"Hello World!"
original_text = original_text.encode('utf-8')
cipher_text = public_key.encrypt(
   original_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Cipher text: {cipher_text}")

cipher_file = original_text.decode('utf-8') + "_cipher_text.bin"
with open(cipher_file, 'wb') as file:
    file.write(cipher_text)

print(f"Cipher file: {cipher_file}")
