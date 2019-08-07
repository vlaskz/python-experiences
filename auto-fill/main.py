import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\sel\\chromedriver.exe")
driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')

termoPesquisa = driver.find_element_by_name('edicao.txtPesquisa')
selecionarTodosOsJornais = driver.find_element_by_id('chk_avancada_0')
dataInicio = driver.find_element_by_name('edicao.dtInicio')
dataFim = driver.find_element_by_id('dt_fim_avancada')
botaoSubmit = driver.find_element_by_id('pesquisa02_0')


termoPesquisa.send_keys('"Isaias Cerqueira Velasquez"')
selecionarTodosOsJornais.click()

dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(0)
dataInicio.send_keys(1)
dataInicio.send_keys(0)
dataInicio.send_keys(1)


botaoSubmit.click()