
print('\033[H\033[J\033[1;34;40m')
print('Pesquisa ao Diário Oficial da União 2019\nDesenvolvido por Vlaskz(www.github.com/vlaskz)\n')

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


print('\033[1;33;40m  --> Iniciando Chrome em modo Headless')
chrome_opt = Options()
chrome_opt.add_argument('--headless')
driver = webdriver.Chrome('C:\\sel\\chromedriver.exe', 0, chrome_opt)
 
print('  --> Acessando site do DOU')
driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')

termoPesquisa = driver.find_element_by_name('edicao.txtPesquisa')
selecionarTodosOsJornais = driver.find_element_by_id('chk_avancada_0')
dataInicio = driver.find_element_by_name('edicao.dtInicio')
dataFim = driver.find_element_by_id('dt_fim_avancada')
botaoSubmit = driver.find_element_by_id('pesquisa02_0')
print('  --> Parametrizando\n')

termoPesquisa.send_keys(input('\033[1;32;40m Pesquisar por: '))
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

print('\n\033[1;33;40m  --> Submetendo informações')
botaoSubmit.click()
print('  --> Processando a saída')
allLinks = driver.find_elements_by_class_name('titulo_jornal')
print('\033[1;33;40m---------------------------------------------------------\033[1;32;40m\n')
print('    ',len(allLinks), ' registro(s) encontrado(s):\n')
for link in allLinks:
    print('   ',link.get_attribute('text'))
    print('     >>>', link.get_attribute('href') ,'\n')
    print('\033[1;33;40m---------------------------------------------------------\033[1;32;40m')
print('\033[1;33;40m  --> Concluído\n')
driver.quit()