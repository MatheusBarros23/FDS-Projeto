from time import time


import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\Users\T-Gamer\Documents\ChromeDriver\chromedriver.exe')
driver.get('https://mprb-y45pa1sk4n81zw2p.socketxp.com')

time.sleep(5)

driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[2]/a').click()

driver.find_element_by_xpath('/html/body/main/div[2]/form/p[1]/input').send_keys("Dzr")

driver.find_element_by_xpath('/html/body/main/div[2]/form/p[2]/input').send_keys("sport03")

driver.find_element_by_xpath('/html/body/main/div[2]/form/p[3]/button').click()