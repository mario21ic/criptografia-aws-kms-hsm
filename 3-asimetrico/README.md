Generar las keys y testeando:
```
./keygen.py my1
./keygen_test.py my1

./keygen.py my2
./keygen_test.py my2
```

Probando cifrado con public key y descifrado con private key:
```
./keygen_test_encrypt.py my2_pub.pem HelloWorld

./keygen_test_decrypt.py my1_priv.pem HelloWorld_cipher_text.bin
./keygen_test_decrypt.py my2_priv.pem HelloWorld_cipher_text.bin
```

Ejecutando:
```
python chat-server.py
python chat-client.py
```
