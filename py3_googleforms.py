#!/usr/bin/python3
#EmreOvunc

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from random import randint
from time import sleep

namefile = open('isimler.txt','r')
names = namefile.readlines()

snamefile = open('soyisim.txt','r')
snames = snamefile.readlines()

def getname(names):
        rast = randint(0,2447)
        if len(names[rast].lower().strip().split(' ')) == 1:
              ad = names[rast].lower().strip()
        else:
              ad = names[rast].lower().strip().split(' ')[1]
        return ad

def getsname(snames):
	rasts = randint(0,2446)
	if len(snames[rasts].lower().strip().split(' ')) == 1:
        	sad = snames[rasts].lower().strip()
	else:
        	sad = snames[rasts].lower().strip().split(' ')[1]
	return sad

def sec():
    option = Options()
    driver_path = "chromedriver"
    option.add_argument('--no-sandbox')
    #option.add_argument('--headless')
    mobile_emulation = {"deviceName": "Nexus 5"} 
    mobile_emulation = {"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },"userAgent": "Mozilla/5.0 (Linux; Android 9; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.62 Mobile Safari/537.36" }
    option.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(executable_path=driver_path,options=option)
    browser.get('URL')
    browser.find_element_by_xpath(".//*[contains(text(), 'User')]").click()

    try:
        ad = getname(names)
    except:
        sec()

    try:
        sad = getsname(snames)
    except:
        sec()

    if 'ş' in ad:
    	ad = ad.replace('ş','s')

    if 'ş' in sad:
            sad = sad.replace('ş','s')

    if 'ğ' in ad:
            ad = ad.replace('ğ','g')

    if 'ğ' in sad:
            sad = sad.replace('ğ','g')

    if 'ü' in ad:
            ad = ad.replace('ü','u')

    if 'ü' in sad:
            sad = sad.replace('ü','u')

    if 'ö' in ad:
            ad = ad.replace('ö','o')

    if 'ö' in sad:
            sad = sad.replace('ö','o')

    if 'ı' in ad:
            ad = ad.replace('ı','i')

    if 'ı' in sad:
            sad = sad.replace('ı','i')

    if 'ç' in ad:
            ad = ad.replace('ç','c')

    if 'ç' in sad:
            sad = sad.replace('ç','c')

    sans = randint(0,1)
    if sans == 0:
    	person  = ad + '_' + sad
    elif sans == 1:
    	person = ad + '.' + sad

    mixed = randint(1000,9999)
    sans_mail = randint(0,3)
    if sans_mail == 0:
            mail = person + str(mixed) + "@gmail.com"
    elif sans == 1:
            mail = person + "@hotmail.com"
    elif sans == 2:
            mail = person + "@outlook.com"
    else:
            mail = person + "@" + ad + sad +".com"

    mail = "test@mail.com"
    browser.find_element_by_name("emailAddress").send_keys(str(mail))
    sleep(1)
    browser.find_element_by_xpath(".//*[contains(text(), 'Gönder')]").click()
    sleep(3)
    browser.close()

sec()