#!/usr/bin/env python

import os
import socket

import hmac
import hashlib


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

text = b"Hello World from Server"

key = b'my_secret_key'
#key = b'otraclave' # para fallar

# Crear un nuevo objeto HMAC para el mensaje original
h_original = hmac.new(key, text, hashlib.sha256)
# HMAC original en formato hexadecimal
original_hmac = h_original.hexdigest()
print(f"Original HMAC: {original_hmac}")

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
                plain_text = data.decode('utf-8')
                print(f"Received from Client: {plain_text!r}")

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

            text_hmac = text.decode('utf-8') + ":" + original_hmac
            conn.sendall(text_hmac.encode('utf-8'))


