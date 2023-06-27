#!/usr/bin/env python
# EdDSA
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/

import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# Generar nueva clave
private_key = ed25519.Ed25519PrivateKey.generate()

# Serializar la clave privada
private_key_file = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    # encoding=serialization.Encoding.PEM,
    # format=serialization.PrivateFormat.OpenSSH,
    encryption_algorithm=serialization.NoEncryption()
)
print(f"private_key_file {private_key_file}")
# Guardar la clave privada en un archivo
with open("ed25519_priv.pem", 'wb') as file:
    file.write(private_key_file)
print("ed25519_priv.pem created")


# Serializar la clave pública para compartirla
public_key = private_key.public_key()
public_key_file = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
    # encoding=serialization.Encoding.OpenSSH, # para otras apps
    # format=serialization.PublicFormat.OpenSSH
)
print(f"public_key_file {public_key_file}")
# Guardar la clave pública en un archivo
with open("ed25519_pub.pem", 'wb') as file:
    file.write(public_key_file)
print("ed25519_pub.pem created")


# Opcional: Cargar las keys desde archivos
with open("ed25519_priv.pem", 'rb') as key_in:
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(key_in.read())
with open("ed25519_pub.pem", 'rb') as key_in:
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(key_in.read())


# Signing
signature = private_key.sign(b"my authenticated message")

# Raises InvalidSignature if verification fails
public_key.verify(signature, b"my authenticated message")
#public_key.verify(signature, b"myss authenticated message") # error

