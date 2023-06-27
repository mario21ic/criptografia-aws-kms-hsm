Generar clave simetrica:
```
./simetric_keygen.py
```

Generar las llaves asimetricas:
```
./asimetric_keygen.py my1
./asimetric_keygen.py my2
```

Cifrar usando la public key y la clave simetrica que cifrara un texto:
```
./main_encrypt.py my2_pub.pem Jm5U2NOuf7JnqqKxuPiNBcntcJ1B-0bfkS5dsbKdeMc= HelloWorld
```

Descrifrar usando la private key para obtener la clave simetrica y asi descifrar el texto:
```
./main_decrypt.py my2_priv.pem encrypted_key.bin cipher_text.bin

./main_decrypt.py my1_priv.pem encrypted_key.bin cipher_text.bin # dara error
```

TODO: hacer un chat para que genere una nueva clave simetrica en cada nueva conexion
