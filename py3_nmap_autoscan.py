#!/usr/bin/python3
# EmreOvunc

from os import system
from socket import inet_aton
from datetime import datetime as dt

ipList = open('ipList.txt', 'r')

try:
    system('rm script_logs.txt 2>/dev/null')
except:
    pass

system('touch script_logs.txt')
logger = open('script_logs.txt', 'w')

IPs    = ipList.readlines()
flag   = 1

forbiddenIP = ['1.1.1.1', '10.0.0.0/24']

for IP in IPs:
    scanIP  = IP.strip()
    try:
        network = scanIP.split('/')[0]
        subnet  = scanIP.split('/')[1]
    except:
        pass

    try:
        inet_aton(network)
    except:
        time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        err1 ='[-]' + str(time) + '|' + str(scanIP) + ' taranamıyor !'
        logger.write(str(err1) + '\n')
        flag = 0

    if flag != 0:
        for ip in forbiddenIP:
            if len(ip.split('/')) > 1:
                nw = ip.split('.')[0] + "." + ip.split('.')[1] + "." + ip.split('.')[2] + "."
                for lastpart in range(0, 256):
                    checkip = nw + str(lastpart)
                    if len(scanIP.split('/')) > 1:
                        if ip == scanIP:
                            time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                            err2 = '[!]' + str(time) + '|' + str(scanIP) + ' yasaklı ! [' + ip + ']'
                            logger.write(str(err2) + '\n')
                            flag = 0
                            break
                        
                    else:
                        if checkip == scanIP:
                            time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                            err3 = '[!]' + str(time) + '|' + str(scanIP) + ' yasaklı ! [' + ip + ']'
                            logger.write(str(err3) + '\n')
                            flag = 0
                            break
            else:
                if ip == scanIP:
                    time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                    err4 = '[!]' + str(time) + '|' + str(scanIP) + ' yasaklı ! [' + ip + ']'
                    logger.write(str(err4) + '\n')
                    flag = 0
                    break

    if flag == 0:
        pass

    else:
        time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        status1 = '[?]' + str(time) + ' | ' + str(scanIP) + ' tarama başlatıldı !'
        logger.write(str(status1) + '\n')
        system('nmap -sV ' + str(scanIP) + ' --open')
        time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        status2 = '[+]' + str(time) + '|' + str(scanIP) + ' tarama bitti !'
        logger.write(str(status2) + '\n')

    flag = 1

ipList.close()
logger.close()
