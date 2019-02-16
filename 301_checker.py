#!/usr/bin/python3
# 301 Checker
# EmreOvunc

from os import popen
from os import system
from re import findall
from time import sleep
from socket import gethostbyname
from multiprocessing import Queue
from multiprocessing import Process


def dns_lookup(host, q):
    try:
        gethostbyname(host)
        q.put(host)
    except:
        pass


system('rm -rf redirected.txt 2</dev/null')
system('rm -rf no_redirect.txt 2</dev/null')
system('rm -rf down_hosts.txt 2</dev/null')

ipFile = "ip_path_from_disk.txt"

ip_file = open(ipFile, "r")
yes     = open("redirected.txt", "a+")
no      = open("no_redirect.txt", "a+")
down    = open('down_hosts.txt', 'a+')

yesArr = []

remaining = int(popen('cat ' + ipFile + '|wc -l').read().strip())

for ip in ip_file:

    if remaining % 10 == 0:
        print('Queue: ' + str(remaining))
    remaining -= 1

    IP = ip.strip()
    if IP != "":
        print('#####', IP, '#####')
        http = 'http://' + str(IP)
        https = 'https://' + str(IP)
        flag = 0

        try:
            http_proc = popen('curl -s -I ' + http + ' --connect-timeout 2 --max-time 2').read()
            if http_proc != "":
                urls = findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', http_proc)
                if http != str(urls[0]) or http != str(urls[0]) + "/":
                    yesArr.append('##### ' + str(IP) + ' #####' + '\n')
                    yesArr.append(http + ' -> ' + str(urls[0]) + '\n')
                    flag += 1
        except:
            pass

        try:
            https_proc = popen('curl -s -I ' + https + ' --connect-timeout 2 --max-time 2').read()
            if https_proc != "":
                urls = findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', https_proc)
                if len(urls[0]) != 0:
                    if https != str(urls[0]) or https != str(urls[0]) + "/":
                        if flag == 0:
                            yesArr.append('##### ' + str(IP) + ' #####' + '\n')
                        yesArr.append(https + ' -> ' + str(urls[0]) + '\n')
                        flag += 1
        except:
            pass

        if flag == 0:
            IPorDomain = findall("^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
                                 "(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", IP)
            if len(IPorDomain) != 0:
                no.write(IP + '\n')
            else:
                q = Queue()
                p = Process(target=dns_lookup, args=(IP, q))
                p.start()
                sleep(1)

                if q.empty():
                    p.terminate()
                    down.write(IP + '\n')
                else:
                    q.get()
                    no.write(IP + '\n')

for index in range(0, len(yesArr)-1):
    if yesArr[index] != "":
        try:
            if yesArr[index].startswith('##### ') and yesArr[index+1].startswith('##### '):
                index += 1
            elif yesArr[index].startswith('##### ') and yesArr[index+1].startswith('http'):
                yes.write(yesArr[index])
                yes.write(yesArr[index+1])
            elif yesArr[index].startswith('http://') and yesArr[index+1].startswith('https://'):
                yes.write(yesArr[index+1])
        except:
            pass

down.close()
yes.close()
no.close()
ip_file.close()
