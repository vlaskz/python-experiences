
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
print('--> Starting Chrome in headless mode\n')
chrome_opt = Options()
chrome_opt.add_argument('--headless')
driver = webdriver.Chrome('C:\\sel\\chromedriver.exe', 0, chrome_opt)
  
driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')
print('--> Accessing website\n')
termoPesquisa = driver.find_element_by_name('edicao.txtPesquisa')
selecionarTodosOsJornais = driver.find_element_by_id('chk_avancada_0')
dataInicio = driver.find_element_by_name('edicao.dtInicio')
dataFim = driver.find_element_by_id('dt_fim_avancada')
botaoSubmit = driver.find_element_by_id('pesquisa02_0')
print('--> Setting values\n')

termoPesquisa.send_keys(input('Search Term: '))
selecionarTodosOsJornais.click()

dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)

dataInicio.send_keys(0)
dataInicio.send_keys(1)
dataInicio.send_keys(0)
dataInicio.send_keys(1)

print('--> Submitting values\n')
botaoSubmit.click()
print('--> Processing output\n')
allLinks = driver.find_elements_by_class_name('titulo_jornal')
print(len(allLinks), ' registro(s) encontrado(s):')
for link in allLinks:
    print(link.get_attribute('href'))
print('--> Job done\n')
driver.quit()