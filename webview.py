from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="D:\Installed\chromedriver.exe")
site = input("Enter site name: ")
driver.get(site.strip())
rate = input("Number of seconds after which site is to be refreshed: ")
refreshrate = int(rate)
count = 0
while True:
    time.sleep(refreshrate)
    driver.refresh()
    count = count+1
    print(count)