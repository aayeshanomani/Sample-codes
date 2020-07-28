from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="D:\Installed\chromedriver.exe")
site = input("Enter site name: ")
driver.get(site)
rate = input("Number of seconds after which site is to be refreshed: ")
refreshrate = int(rate)

while True:
    time.sleep(refreshrate)
    driver.refresh()