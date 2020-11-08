from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import PKCS1_v1_5
from Crypto.Util.Padding import pad, unpad
import random


def generateAesKey():
    session_key = get_random_bytes(16)
    return session_key


def encryptMessage(message, aes_key, mode=AES.MODE_ECB):
    cipher_aes = AES.new(aes_key, mode)
    ciphertext = cipher_aes.encrypt(pad(message, 16))
    return ciphertext


def decryptMessage(message, aes_key, mode=AES.MODE_ECB):
    cipher_aes = AES.new(aes_key, mode)
    data = cipher_aes.decrypt(message)
    return data


def decryptMessagek3(message, aes_key, mode=AES.MODE_ECB):
    cipher_aes = AES.new(aes_key, mode)
    data = unpad(cipher_aes.decrypt(message), 16)
    return data


k3_file = "NotASecretFile.txt"


def read_k3():
    f = open(k3_file, "rb")
    k3 = f.read()
    return k3


def get_mode():
    return "ECB" if random.randint(0, 1) else "CFB"

