from time import time


import time
from selenium import webdriver

##Teste para abrir o site
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
driver.get('https://mprb-y45pa1sk4n81zw2p.socketxp.com')
start_time = time.time() #count start time
driver.maximize_window()
time.sleep(5)

##Testando o botão 'Novo Jogo'
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[2]/a').click()
##Preenchendo credenciais de nome e senha
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[1]/input').send_keys("Dzr")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[2]/input').send_keys("sport03")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[3]/button').click()


#Adicionando um jogo
driver.find_element_by_xpath('//*[@id="nome"]').send_keys("CS:GO")
driver.find_element_by_xpath('//*[@id="categoria"]').send_keys("FPS")
driver.find_element_by_xpath('//*[@id="console"]').send_keys("PC")
driver.find_element_by_xpath('//*[@id="critica"]').send_keys("The best game in History")
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()

##Testando o botão 'Novo Jogo' quando já logado
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[2]/a').click()

#Adicionando outro jogo
driver.find_element_by_xpath('//*[@id="nome"]').send_keys("Celeste")
driver.find_element_by_xpath('//*[@id="categoria"]').send_keys("Plataforma")
driver.find_element_by_xpath('//*[@id="console"]').send_keys("PC")
driver.find_element_by_xpath('//*[@id="critica"]').send_keys("Celeste é a montanha a ser escalada, mas também é muito mais do que isso. Em um raro game em que todas as parcelas se alinham perfeitamente, o que começa como um quebra-cabeça e plataforma, termina como uma jornada cheia de detalhes e pequenas poesias. Entre o correr e o habitar, Celeste apresenta diversos duplos complementares, e se torna uma das melhores surpresas que joguei. Por favor, me mande morangos.")
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()

##Testando o botão 'Excluir'
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/table/tbody/tr[7]/td[5]/a').click()

##Testando o botão 'Editar'
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/table/tbody/tr[5]/td[4]/a').click()
driver.find_element_by_xpath('//*[@id="nome"]').send_keys(" Houses")
driver.execute_script("window.scrollTo(0, 780)")
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/main/form/fieldset/button').click()


##Testando o botão 'Logout'
time.sleep(2)
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[4]/a').click()

##Testando o 'video do youtube'
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/div[2]/iframe').click()
time.sleep(4)
driver.find_element_by_xpath('/html/body/main/div[2]/iframe').click()

##Testando o '2 video do youtube'
driver.find_element_by_xpath('/html/body/main/div[3]/iframe').click()
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(5)
driver.find_element_by_xpath('/html/body/main/div[3]/iframe').click()


##Testando adição de 'novo jogo' sem nome, categoria ou console
driver.execute_script("window.scrollTo(1080, 0)")
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[2]/a').click()

##Preenchendo credenciais de nome e senha
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[1]/input').send_keys("Kryno")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[2]/input').send_keys("4321")
driver.find_element_by_xpath('/html/body/main/div[2]/form/p[3]/button').click()

#tela novo jogo
driver.execute_script("window.scrollTo(0, 780)")
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="nome"]').send_keys("Ghostwire: Tokyo")

driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="categoria"]').send_keys("RPG")

driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="console"]').send_keys("Playstation 5")

driver.find_element_by_xpath('//*[@id="critica"]').send_keys("Fãs do terror japonês vão se deleitar com todo o trabalho feito em Ghostwire: Tokyo, do design das criaturas até o cuidado com a ambientação. Quem esperava um jogo de terror genuíno, mais puxado para os survival horrors tradicionais pelos quais Mikami é conhecido, como Resident Evil ou The Evil Within, pode se decepcionar um pouco, afinal, este é um game de ação e aventura.")
driver.execute_script("window.scrollTo(0, 720)")
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/form/fieldset/button').click()
driver.find_element_by_xpath('/html/body/main/table/tbody/tr[9]/td[5]/a').click()

teste = driver.find_element_by_xpath('/html/body/header/div[1]/ul/li').text
assert teste == "O jogo foi removido com sucesso!", "error"
end_time = time.time() #count end time

if teste == "O jogo foi removido com sucesso!":
    exec_time = end_time - start_time
    print('All tests passed')
    print('----------------------------------------------------------------------')
    print(f"Ran 14 tests in {exec_time:.2f} seconds")

print('OK')

driver.quit()