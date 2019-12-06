#!/usr/bin/python3

from socket import gethostbyaddr
from os import system
from subprocess import Popen, PIPE

## Current configuration is designed to discover
## hostname and web url to given IP 0-255 (means /24)
## If you want to scan /16 instead of /24, you should
## change last_subnet to 255 or other one.
## last_subnet is on line #84.

## IP = Network ID
## Examples:
## /24 = 192.168.1.0
## /16 = 192.168.0.0

IP = "10.0.0.0"
List = []
webList = []
path = '/root/Desktop/ip2hostname_web'
system('mkdir ' + path)

def httpHeaders(IP):
    nmapScript = 'nmap --script http-headers -p80,443 ' + IP +' -T5 |grep Location |grep -v "' + IP + '"'
    nmapProc = Popen([nmapScript], stdout=PIPE, shell=True)
    (out, err) = nmapProc.communicate()
    if out.decode() != "":
        webList.append((IP, out.decode().split()[2]))

def writewebList(list):
    file_web = open(path + '/webhost.txt', 'w')
    file_ip2web = open(path + '/ip2web.txt', 'w')
    for webip in list:
        file_web.write(str(webip[1]))
        file_ip2web.write(str(webip[0] + '|' + str(webip[1])))
    file_web.close()
    file_ip2web.close()

def writeList(list):
    file_ip = open(path + '/ip_list.txt', 'w')
    file_host = open(path + '/host_list.txt', 'w')
    file_ip2host = open(path  + '/ip2host.txt', 'w')
    for ips in list:
        if not 'Unkn' in str(ips).split(' ')[0][2:-2]:
            file_ip.write(str(ips).split(' ')[2][2:-3])
            file_host.write(str(ips).split(' ')[0][2:-2])
            file_ip2host.write(str(ips).split(' ')[2][2:-3] + '|' + str(ips).split(' ')[0][2:-2])
    file_ip.close()
    file_host.close()
    file_ip2host.close()

def gethostname(IPaddr):
    try:
        List.append(gethostbyaddr(IPaddr))
    except:
        List.append(('Unknown Host', [], IPaddr))


subnet = IP.split('.')[0] + '.' +\
         IP.split('.')[1] + '.'

target = IP.split('.')[0] + '.' +\
         IP.split('.')[1] + '.' +\
         IP.split('.')[2] + '.'

last_subnet = int(IP.split('.')[2])
last_part = int(IP.split('.')[3])

while True:
    last_part += 1 if last_part < 255 else -255
    temp_IP = str(subnet) + str(last_subnet)+ '.' + str(last_part)

    gethostname(temp_IP)
    httpHeaders(temp_IP)

    if last_part == 255:
        last_subnet += 1

    ## Change it if you want to discover another subnet.
    ## For Example: IP = 10.250.180.0 
    ## /24 -> last_subnet = 181
    ## /16 -> last_subnet = 256
    if last_subnet == 256:
        break

writeList(List)
writewebList(webList)