from hashlib import sha256
from Crypto.Cipher import AES

def get_key(passphrase: str) -> bytes:
    # Derive a 32-byte key from passphrase using SHA-256
    return sha256(passphrase.encode('utf-8')).digest()

def encrypt(data: bytes, passphrase: str) -> bytes:
    key = get_key(passphrase)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # Store nonce + tag + ciphertext together
    encrypted = cipher.nonce + tag + ciphertext
    return encrypted

def decrypt(encrypted: bytes, passphrase: str) -> bytes:
    key = get_key(passphrase)
    nonce = encrypted[:16]
    tag = encrypted[16:32]
    ciphertext = encrypted[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data
