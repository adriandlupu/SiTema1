import socket
from time import sleep
from crypto_utils import *

KG_HOST = '127.0.0.1'
KG_PORT = 65477
B_HOST = '127.0.0.1'
B_PORT = 65478

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((KG_HOST, KG_PORT))
    mod_criptare = get_mode()
    k3 = read_k3()
    s.send(encryptMessage(bytearray(mod_criptare, "utf-8"), k3))
    message = s.recv(2048)
    cheie = decryptMessagek3(message, k3)
    print(cheie)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((B_HOST, B_PORT))
    s.send(encryptMessage(bytearray(mod_criptare, "utf-8"), k3))
    sleep(1)
    s.send(encryptMessage(cheie, k3))
    mode = AES.MODE_ECB if mod_criptare == "ECB" else AES.MODE_CFB

    mesaj = decryptMessage(s.recv(2048), cheie, mode)
    print(str(mesaj, "utf-8"))
    f = open("mesajNeSecret.txt", "r")
    mesajnesecret = f.read()
    s.send(encryptMessage(bytearray(mesajnesecret, "utf-8"), cheie, mode))
