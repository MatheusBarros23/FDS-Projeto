from time import time


import time
from selenium import webdriver

##Teste para abrir o site
driver = webdriver.Chrome(executable_path=r'C:\Users\T-Gamer\Documents\ChromeDriver\chromedriver.exe')
driver.get('https://mprb-y45pa1sk4n81zw2p.socketxp.com')

time.sleep(5)

##Testando o botão 'Novo Jogo'
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[2]/a').click()
##Preenchendo credenciais de nome e senha
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[1]/input').send_keys("Dzr")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[2]/input').send_keys("sport03")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[3]/button').click()

#Adicionando o novo jogo
driver.find_element_by_xpath('//*[@id="nome"]').send_keys("CS:GO")
driver.find_element_by_xpath('//*[@id="categoria"]').send_keys("FPS")
driver.find_element_by_xpath('//*[@id="console"]').send_keys("PC")
driver.find_element_by_xpath('//*[@id="critica"]').send_keys("The best game in History")
driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()



