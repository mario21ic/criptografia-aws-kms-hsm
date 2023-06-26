#!/usr/bin/env python

import os
import socket


from cryptography.fernet import Fernet


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
text = b"Hello World from Client"

#key = Fernet.generate_key()
#key = "QIRqW5PdDLyEEi4EBKaVfRi-X11rg5-GpG1YX3qS-_M="
key = os.environ['KEY_SECRET']
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(text)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello, world")
    #s.sendall(text)
    s.sendall(cipher_text)
    data = s.recv(1024)

plain_text = cipher_suite.decrypt(data)
print(f"Received from Server: {plain_text!r}")
