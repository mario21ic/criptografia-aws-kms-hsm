#!/usr/bin/env python

import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

file_name = "default"
if len(sys.argv)>= 1:
    file_name = sys.argv[1]
print(f"Files: {file_name}_*.pem")

# Cargar las keys
with open(file_name + "_priv.pem", 'rb') as pem_in:
    private_key = serialization.load_pem_private_key(pem_in.read(), password=None)

with open(file_name + "_pub.pem", 'rb') as pem_in:
    public_key = serialization.load_pem_public_key(pem_in.read())


# Cifrar un mensaje
original_text = b"Hello World!"
cipher_text = public_key.encrypt(
   original_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Cipher text: {cipher_text}")

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
