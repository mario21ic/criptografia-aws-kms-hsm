#!/usr/bin/env python

import os
import socket

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Cargando mi private key
with open("my1_priv.pem", 'rb') as pem_in:
    my_private_key = serialization.load_pem_private_key(pem_in.read(), password=None)

# Cargando public key del destino
with open('my2_pub.pem', 'rb') as pem_in:
    dest_public_key = serialization.load_pem_public_key(pem_in.read())


# Cifrando mensaje con pub key del destino
original_text = b"Hello World from Server"
cipher_text = dest_public_key.encrypt(
   original_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                # Descifrar el mensaje
                plain_text = my_private_key.decrypt(
                   data,
                   padding.OAEP(
                       mgf=padding.MGF1(algorithm=hashes.SHA256()),
                       algorithm=hashes.SHA256(),
                       label=None
                   )
                )
                print(f"Received from Client: {plain_text!r}")

            conn.sendall(cipher_text)

#print(f"Received from Client: {data!r}")

