#!/usr/bin/env python
# EcDSA
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization



private_key = ec.generate_private_key(
    ec.SECP384R1()
)

# Serializar la clave privada
serialized_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'testpassword')
)
print(f"serialized_private {serialized_private}")
# Guardar la clave privada en un archivo
with open("ecdsa_priv.pem", 'wb') as file:
    file.write(serialized_private)
print("ecdsa_priv.pem created")

# Serializar la clave pública
public_key = private_key.public_key()
serialized_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"serialized_public {serialized_public}")
# Guardar la clave pública en un archivo
with open("ecdsa_pub.pem", 'wb') as file:
    file.write(serialized_public)
print("ecdsa_pub.pem created")


# Opcional: Cargar las keys desde archivos
with open("ecdsa_priv.pem", 'rb') as key_in:
    private_key = serialization.load_pem_private_key(
        key_in.read(),
        # or password=None, if in plain text
        password=b'testpassword',
    )

with open("ecdsa_pub.pem", 'rb') as key_in:
    public_key = serialization.load_pem_public_key(
        key_in.read(),
    )

# Signing
data = b"this is some data I'd like to sign"
signature = private_key.sign(
    data,
    ec.ECDSA(hashes.SHA256())
)

# Verification
public_key.verify(signature, b"this is some data I'd like to sign", ec.ECDSA(hashes.SHA256()))
# public_key.verify(signature, b"this is some data I'd like to sign xD", ec.ECDSA(hashes.SHA256())) # error
