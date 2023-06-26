#!/usr/bin/env python

import os
import socket

from cryptography.fernet import Fernet


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
text = b"Hello World from Server"

#key = Fernet.generate_key()
#key = "QIRqW5PdDLyEEi4EBKaVfRi-X11rg5-GpG1YX3qS-_M="
key = os.environ['KEY_SECRET']
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(text)

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
                #print("data", data)
                #print(f"Received from Client: {data!r}")
                plain_text = cipher_suite.decrypt(data)
                print(f"Received from Client: {plain_text!r}")

            #conn.sendall(data) # reply
            #conn.sendall(text)
            conn.sendall(cipher_text)

