```
export KEY_SECRET="MvJGv09gMnTnKSQbvQo1RBGeuiE72BSAqwWNQk9cluA="
python chat-server.py
python chat-client.py
```

Now try to with a different key on client side running this code:
```
export KEY_SECRET=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())")
python chat-client.py
```
