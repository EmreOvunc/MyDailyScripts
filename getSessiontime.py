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
	for i in range(10):
		sleep(0.001)
		t = Thread(target=getTime)
		t.start()

def getTime():
	while True:
		try:
			response = head(url, cookies=cookies)
			if (response.headers['Set-Cookie'].split(";")[0][:4]) != "Last":
				print(response.headers['Set-Cookie'].split(";")[2].split(',')[1].strip())
			else:
				print(response.headers['Set-Cookie'].split(";")[0].strip())
		except:
			pass

jobs = []

url = "URL"
cookies = {'sessionID':'testCookie'}

for i in range(5):
    p = Process(target=threads)
    jobs.append(p)
    p.start()