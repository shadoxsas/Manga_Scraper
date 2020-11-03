# import

# main

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#import pyautogui

def sleep(a):
    time.sleep(a)

#const with a path to webdriver
driver = webdriver.Chrome(r'A:/Scraping/chromedriver.exe')

sleep(2)

driver.get("https://9gag.com")

sleep(2)

#screenshot
#myScreenshot = pyautogui.screenshot()
#myScreenshot.save(r'C:\Users\Shadoxsas\Desktop\screenshot1.png')

#quit
driver.quit()