import socket,os,time

host = "ServerIP"
port = "ServerPORT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("EmreOvunc-Disk")
if (os.path.isdir("df-h.txt")):
    os.remove("df-h.txt")
time.sleep(1)
os.system("df -h > df-h.txt")
time.sleep(1)
f = open('df-h.txt', 'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
f.close()
s.close()
os.system("rm -rf /home/monster/df-h.txt")
