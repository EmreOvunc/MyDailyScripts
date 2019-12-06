#!/usr/bin/python3
#EmreOvunc

from os import listdir
from os import system

system('rm ms17_010.txt 2</dev/null')
system('rm cve2009_3103.txt 2</dev/null')

filePath = '/root/smb_vuln/'
fileList = listdir(filePath)

whitelist4file = 'nmap'
newList = []

system('touch ms17_010.txt')
ms17_010 = open('ms17_010.txt', 'a')

system('touch cve2009_3103.txt')
cve2009_3103 = open('cve2009_3103.txt', 'a')

searchVulnerability1='Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)'
searchVulnerability2='SMBv2 exploit (CVE-2009-3103, Microsoft Security Advisory 975497)'

for file in fileList:
    if(file.split('.')[4] == str(whitelist4file)):
        newList.append(file)

for newFile in newList:
    readFile = open(str(filePath+newFile), 'r')
    lines = readFile.readlines()
    for line in lines:
        if searchVulnerability1 in line:
            ms17_010.write(str(newFile[:-5])+'\n')
        if searchVulnerability2 in line:
            cve2009_3103.write(str(newFile[:-5])+'\n')

ms17_010.close()
cve2009_3103.close()
