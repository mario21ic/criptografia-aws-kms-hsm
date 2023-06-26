#!/usr/bin/env python

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

text = b"Hello World from Server"
#data = None

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
                print(f"Received from Client: {data!r}")
            #conn.sendall(data)
            conn.sendall(text)

#print(f"Received from Client: {data!r}")

