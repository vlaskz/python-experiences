
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_opt = Options()
chrome_opt.add_argument('--headless')
driver = webdriver.Chrome('C:\\sel\\chromedriver.exe', 0, chrome_opt)
  
driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')
#print('abrindo url')
termoPesquisa = driver.find_element_by_name('edicao.txtPesquisa')
selecionarTodosOsJornais = driver.find_element_by_id('chk_avancada_0')
dataInicio = driver.find_element_by_name('edicao.dtInicio')
dataFim = driver.find_element_by_id('dt_fim_avancada')
botaoSubmit = driver.find_element_by_id('pesquisa02_0')
#print('pagina capturada')

termoPesquisa.send_keys('"Isaias Cerqueira Velasquez"')
selecionarTodosOsJornais.click()
#print('setando nome')
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)
dataInicio.send_keys(Keys.BACKSPACE)

dataInicio.send_keys(0)
dataInicio.send_keys(1)
dataInicio.send_keys(0)
dataInicio.send_keys(1)
#print('setando data_inicio')

botaoSubmit.click()
#print('submetendo os dados')
time.sleep(5)
#print('nova URL:', driver.current_url, )
allLinks = driver.find_elements_by_class_name('titulo_jornal')
print(len(allLinks), ' registro(s) encontrado(s)')
for link in allLinks:
    print(link.get_attribute('href'))
#print('fechando tudo e saindo')
driver.quit()