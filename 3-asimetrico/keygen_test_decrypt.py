#!/usr/bin/env python
# Example: ./keygen_test_decrypt.py my2_priv.pem HelloWorld_cipher_text.bin

import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

file_name = "default"
if len(sys.argv)>= 1:
    file_name = sys.argv[1]
print(f"Key file: {file_name}")

file_o = open(sys.argv[2], 'rb')
cipher_text = file_o.read()
print(f"Texto to decrypt: {cipher_text}")

# Cargar las keys
with open(file_name, 'rb') as pem_in:
    private_key = serialization.load_pem_private_key(pem_in.read(), password=None)

# Descifrar el mensaje
plain_text = private_key.decrypt(
   cipher_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Plain text: {plain_text.decode()}")
