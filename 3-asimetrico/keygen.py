#!/usr/bin/env python

import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

file_name = "default"
if len(sys.argv)>= 1:
    file_name = sys.argv[1]

# Generar un par de claves
private_key = rsa.generate_private_key(
   public_exponent=65537,
   key_size=2048,
)

private_key_file = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
#print("private_key_file", private_key_file)
with open(file_name + "_priv.pem", 'wb') as file:
    file.write(private_key_file)


# Serializar la clave pública para compartirla
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
#print("public_pem", public_pem)
with open(file_name + "_pub.pem", 'wb') as file:
    file.write(public_pem)

