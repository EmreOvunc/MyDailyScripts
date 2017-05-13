import socket,os,time

host = "SERVERIP"
port = "SERVERPORT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("EmreOvunc-ArpA")
if (os.path.isdir("arp-a.txt")):
    os.remove("arp-a.txt")
time.sleep(1)
os.system("sudo arp -a > arp-a.txt")
time.sleep(1)
f = open('arp-a.txt', 'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
f.close()
s.close()
os.system("rm -rf /home/monster/arp-a.txt")
