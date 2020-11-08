import socket
from crypto_utils import generateAesKey, encryptMessage, decryptMessage, k3_file, read_k3, decryptMessagek3
import random
HOST = '127.0.0.1'
PORT = 65477
k1 = ""
k2 = ""
k3 = ""


def generate_k3():
    global k3
    k3 = generateAesKey()
    file_out = open(k3_file, "wb")
    file_out.write(k3)
    file_out.close()


def generate_k1():
    global k1
    k1 = generateAesKey()


def generate_k2():
    global k2
    k2 = generateAesKey()


def get_key(mod_criptare):
    if mod_criptare == "ECB":
        return k1
    else:
        return k2


if __name__ == '__main__':
    generate_k1()
    generate_k2()
    generate_k3()

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print("Waiting for connection...")
            conn, _ = s.accept()
            mod = decryptMessagek3(conn.recv(2048), k3)
            the_key = get_key(str(mod))
            conn.send(encryptMessage(the_key, k3))
