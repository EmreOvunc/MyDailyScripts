#!/usr/bin/python3
#EmreOvunc

#########################
# pip3 install requests #
#########################

from multiprocessing    import Process
from multiprocessing    import Queue
from threading          import Thread
from requests           import get
from time               import sleep
from re                 import findall

def findDuplicates(publicQueue, crawlingQueue, controlQueue, website, domain, urlFile):
	#qList for temp. URLs
	qList = []
	addFlag = 0
	
	#Add first address to the list.
	qList.append(website)

	while True:
		if not publicQueue.empty():
			tmpURL = publicQueue.get()

			for oldURL in qList:

				#If the URL come already.
				if oldURL == tmpURL:
					addFlag += 1
					break

			if addFlag == 0:

				#Controlling domain part
				if domain in tmpURL:
					urlFile.write(tmpURL + "\n")
					qList.append(tmpURL)
					crawlingQueue.put(tmpURL)

			else:
				addFlag -= 1

		else:
			sleep(0.05)

		#If the crawling done!
		if controlQueue.empty():
			break

	urlFile.close()


def findURLs(publicQueue, crawlingQueue, controlQueue, baseURL, domain):
	while True:

		#If crawling url not found!
		if crawlingQueue.empty() and not publicQueue.empty():
			pass

		#If all queues are empty, stop crawling processes.
		elif publicQueue.empty() and crawlingQueue.empty():
			controlQueue.get()
			exit(0)

		else:
			website = crawlingQueue.get()

			try:
				response = get(website)
				#response = get(website, cookies=cookies)
			except:
				response = "ERROR"

			try:
				content  = response.content.decode('utf-8')
			except:
				content  = ""

			urls = findall(r'href=[\'"]?([^\'" >]+)', content)

			for url in urls:

				#Hardcoded elimination for urls
				if "javascript:void(0)" != url.strip() and '#' != url.strip():

					#Checking the url .css or .js extension
					if url.strip().split(".")[-1] != "js" 		and url.strip().split(".")[-1] != "css"		\
					   and url.strip().split(".")[-1] != "png"  and url.strip().split(".")[-1] != "json" 	\
					   and url.strip().split(".")[-1] != "jpeg" and url.strip().split(".")[-1] != "jpg" 	\
					   and url.strip().split(".")[-1] != "xml"  and url.strip().split(".")[-1] != "co" 		\
					   and url.strip().split(".")[-1] != "pdf"  and url.strip().split(".")[-1] != "rb" 		\
					   and url.strip().split(".")[-1] != "py"   and url.strip().split(".")[-1] != "c" 		\
					   and url.strip().split(".")[-1] != "svg" 	and url.strip().split(".")[-1] != "ico"		:

						#If the url is not in the http:// or https:// (base) format
						if not url.startswith(baseURL):

							#Passing mail 
							if not url.startswith('mailto'):
							
								#If the URL is different from the target domain
								if not url.startswith('http'):

									#It prevents double // -> http://example.com//path
									if not url.startswith("/"):

										#Concatenate domain + url
										url = baseURL + "/" + url

									else:

										#Concatenate domain + url
										url = baseURL + url

						else:

							#Controlling domain part
							if not domain in url:
								break

						#Controlling via blackList
						blackFlag = 0
						for site in blackList:

							if site in url:
								blackFlag += 1
								break

						#blackFlag = 0 means, the URL is valid
						if blackFlag == 0:
								publicQueue.put(url)
						
						#Else, the url is in the blacklist.
						else:
							blackFlag -= 1

#Multi-processing
publicQueue   = Queue(maxsize=5000)
crawlingQueue = Queue(maxsize=5000)
controlQueue  = Queue(maxsize=2)

controlQueue.put(1)

#Write results in to the file
urlFile = open('urlFiles.txt','w')

#Do not put these urls into the Queue!
blackList = ["microsoft.com", "google.com", "mozilla.org", "instagram.com",\
			 "linkedin.com", "twitter.com", "github.com", "facebook.com"]

#Starting address for crawling

baseURL = "https://example.com"
website = "https://example.com"
domain  = "example.com"

'''
#Change burp_cookie value to active session cookies!!!
burp_cookie = ""
burp_cookie = burp_cookie[8:]

#New cookies in JSON format
cookies = {}

#Convert cookie to JSON 
for numberofcookies in range (0, len(burp_cookie.split(";"))):
	cookies[burp_cookie.split(";")[numberofcookies].split("=")[0].strip()] =\
			burp_cookie.split(";")[numberofcookies].split("=")[1].strip()
'''

#Put first URL into the crawling queue
crawlingQueue.put(website)

#Finding URLs
url_proc = Process(target=findURLs, args=(publicQueue, crawlingQueue, controlQueue, baseURL, domain, ) )
url_proc.start()

#Finding duplicates
dup_proc = Process(target=findDuplicates, args=(publicQueue, crawlingQueue, controlQueue, website, domain, urlFile, ) )
dup_proc.start()

while True:
	#If all processes are done!
	if not url_proc.is_alive() and not url_proc.is_alive():
		exit()
