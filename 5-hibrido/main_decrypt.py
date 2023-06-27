#!/usr/bin/env python
# Syntax: ./main_decrypt.py private_key_file encrypted_key_file cipher_text_file
# Example: ./main_decrypt.py my2_priv.pem encrypted_key.bin cipher_text.bin

import os
import sys

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import base64

private_key_file = "default"
if len(sys.argv)>= 1:
    private_key_file = sys.argv[1]
print(f"Key file: {private_key_file}")

encrypted_key_file = open(sys.argv[2], 'rb')
encrypted_key = encrypted_key_file.read()
print(f"Asimetric key to decrypt: {encrypted_key}")

cipher_text_file = open(sys.argv[3], 'rb')
cipher_text = cipher_text_file.read()
print(f"Text to decrypt: {cipher_text}")

# Load private key from file
with open(private_key_file, 'rb') as pem_in:
    private_key = serialization.load_pem_private_key(pem_in.read(), password=None)

# El receptor puede usar su clave privada para desencriptar la clave simétrica
decrypted_asimetric_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Y luego usar la clave simétrica desencriptada para desencriptar el mensaje
cipher_suite = Fernet(decrypted_asimetric_key)
plain_text = cipher_suite.decrypt(cipher_text)

print(f"Plain text: {plain_text}")  # Debería imprimir: b'mensaje secreto'

