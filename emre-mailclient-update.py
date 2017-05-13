import socket

# Emre Ovunc
# info@emreovunc.com

HOST = 'SERVERIP'
PORT = 'SERVERPORT'

def socket_func():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('EmreOvunc-Update')
    s.close()

socket_func()
