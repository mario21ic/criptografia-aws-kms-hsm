#!/usr/bin/env python

import os
import socket


import hmac
import hashlib


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

text = b"Hello World from Client"

key = b'my_secret_key'
#key = b'otraclave' # para fallar

# Crear un nuevo objeto HMAC para el mensaje original
h_original = hmac.new(key, text, hashlib.sha256)
# HMAC original en formato hexadecimal
original_hmac = h_original.hexdigest()
print(f"Original HMAC: {original_hmac}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text_hmac = text.decode('utf-8') + ":" + original_hmac
    s.sendall(text_hmac.encode('utf-8'))
    data = s.recv(1024)


plain_text = data.decode('utf-8')
print(f"Received from Server: {plain_text!r}")

plain_text_split = plain_text.split(":")

# Obteniendo hmac
received_hmac = plain_text_split[1] # este debería ser el HMAC recibido
message = plain_text_split[0]

# Crear un nuevo objeto HMAC para el mensaje recibido
new_h_received = hmac.new(key, message.encode('utf-8'), hashlib.sha256)

# Comprobando
if hmac.compare_digest(new_h_received.hexdigest(), received_hmac):
    print("El mensaje recibido ES auténtico.")
else:
    print("El mensaje recibido NO es auténtico.")
