#!/usr/bin/env python

from cryptography.fernet import Fernet

# Generación de clave simétrica
print(Fernet.generate_key().decode('utf-8'))