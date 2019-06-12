#!/usr/bin/python3
#EmreOvunc

#########################
# pip3 install requests #
#########################

from multiprocessing import Process
from threading import Thread
from requests import head
from time import sleep

def threads():
	for i in range(15):
		sleep(0.001)
		t = Thread(target=getTime)
		t.start()

def getTime():
	response = head(url)
	print(response.headers['Set-Cookie'].split(";")[0])
	#print(response.headers['Date'])

jobs = []

url = "URL"

for i in range(5):
    p = Process(target=threads)
    jobs.append(p)
    p.start()