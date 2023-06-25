#!/usr/bin/env python

import os
import socket

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


# Cargando mi private key
with open("my2_priv.pem", 'rb') as pem_in:
    my_private_key = serialization.load_pem_private_key(pem_in.read(), password=None)

# Cargando public key del destino
with open('my1_pub.pem', 'rb') as pem_in:
    dest_public_key = serialization.load_pem_public_key(pem_in.read())


# Cifrando mensaje con pub key del destino
original_text = b"Hello World from Client xD"
cipher_text = dest_public_key.encrypt(
   original_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(cipher_text)
    data = s.recv(1024)

plain_text = my_private_key.decrypt(
   data,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Received from Server: {plain_text!r}")

