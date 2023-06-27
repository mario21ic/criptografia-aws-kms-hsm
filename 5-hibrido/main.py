#!/usr/bin/env python


from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import base64

# Generación de par de claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Serialización de la clave pública
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generación de clave simétrica
key_fernet = Fernet.generate_key()
cipher_suite = Fernet(key_fernet)

# Encriptación del mensaje con clave simétrica
data = b"clave-para-cifrado-simetrico"
cipher_text = cipher_suite.encrypt(data)

# Encriptación de la clave simétrica con la clave pública RSA
encrypted_key = public_key.encrypt(
    key_fernet,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# RECEPTOR:
# Ahora el cifrado y la clave encriptada se pueden enviar al receptor
# El receptor puede usar su clave privada para desencriptar la clave simétrica
decrypted_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Y luego usar la clave simétrica desencriptada para desencriptar el mensaje
cipher_suite = Fernet(decrypted_key)
plain_text = cipher_suite.decrypt(cipher_text)

print(f"plain_text: {plain_text}")  # Debería imprimir: b'mensaje secreto'

