from scapy.all import *

qName="emreovunc.com"
dnsServer="8.8.8.8"

answer = sr1(IP(dst=dnsServer)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=qName)),verbose=1)

print answer[DNS].summary()
