# import modules

from selenium import webdriver
from requests import get
from selenium.webdriver.chrome.service import Service
import time

#manga_site_base
    #manga_site_list = ['mangareader.net', 'hayate.eu']
#manga's_list
    #manga_list = ['tate-no-yuusha-no-nariagari']

#user request
driver_path = 'A:/Scraping/chromedriver.exe'

#start Chrome
service = Service(driver_path)
service.start()

#Chrome_auto

time.sleep(10)
wd.get("https://9gag.com")
time.sleep(10)
wd.back()
time.sleep(10)


#quit Chrome
wd = webdriver.Remote(service.service_url)
wd.quit()

#Closing process
#print(input("Type any key to close. Thank you for using my program"))

