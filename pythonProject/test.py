from flask import Flask, render_template, request
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("process.env.PORT")
navegador.find.element_by_xpath('/html/body/header/div[2]/nav/ul/li[1]/a').click()
time.sleep(5)
