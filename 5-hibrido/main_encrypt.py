#!/usr/bin/env python
# Syntax: ./hibrido_encrypt.py public_key_file asimetric_key string-to-encrypt
# Example: ./hibrido_encrypt.py my2_pub.pem Jm5U2NOuf7JnqqKxuPiNBcntcJ1B-0bfkS5dsbKdeMc= HelloWorld


import os
import sys

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet


public_key_file = sys.argv[1]
print(f"Key file: {public_key_file}")

asimetric_key = sys.argv[2].encode('utf-8')
print(f"Asimetric key: {asimetric_key}")

original_text = "HelloWorld"
if len(sys.argv)>= 3:
    original_text = sys.argv[3].encode('utf-8')
print(f"Texto to encrypt: {original_text}")


# Load keys
with open(public_key_file, 'rb') as pem_in:
    public_key = serialization.load_pem_public_key(pem_in.read())
cipher_suite = Fernet(asimetric_key)


# Encriptación de la clave simétrica con la clave pública RSA
encrypted_key = public_key.encrypt(
    asimetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"encrypted_key: {encrypted_key}")
with open("encrypted_key.bin", 'wb') as file:
    file.write(encrypted_key)
print("encrypted_key.bin created")

# Encriptación del mensaje con clave simétrica
cipher_text = cipher_suite.encrypt(original_text)
print(f"cipher_text: {cipher_text}")
with open("cipher_text.bin", 'wb') as file:
    file.write(cipher_text)
print("cipher_text.bin created")