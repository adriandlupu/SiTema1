import socket
from crypto_utils import *

KG_HOST = '127.0.0.1'
KG_PORT = 65477
B_HOST = '127.0.0.1'
B_PORT = 65478
k3 = read_k3()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((B_HOST, B_PORT))
    s.listen()
    conn, _ = s.accept()
    mod = decryptMessagek3(conn.recv(2048), k3)
    print(mod)
    cheie = decryptMessagek3(conn.recv(2048), k3)
    print(cheie)
    mode = AES.MODE_ECB if mod == "ECB" else AES.MODE_CFB
    conn.send(encryptMessage(bytearray("ok", "utf-8"), cheie, mode))
    mesajnesecret=decryptMessage(conn.recv(2048), cheie, mode)
    print(str(mesajnesecret, "utf-8"))

