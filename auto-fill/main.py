from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

# with open('data.json') as json_file:
#   data = json.load(json_file)

#ciclo do programa:
    #mostrar texto de apresentação
    #inicializar o driver
    #conectar ao site e obter os objetos
    #carregar os dados do prompt ou do data.json
        #se for via prompt, executar e sair
        #se for via data.json, fazer uma pesquisa para cada registro
    #exibir os registros armazenados
#sair
def presentation():

    print('\033[H\033[J\033[1;34;40m')
    print('Bot para Pesquisa ao Diário Oficial da União 2019\nDesenvolvido por Vlaskz(https://github.com/vlaskz)\n')


def initialize():
    print('\033[1;33;40m  --> Inicializando')
    chrome_opt = Options()
    chrome_opt.add_argument('--headless')
    driver = webdriver.Chrome('C:\\sel\\chromedriver.exe', 0, chrome_opt)
    return driver


def connect(driver):
    print('  --> Conectando')
    driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')
    searchString               = driver.find_element_by_name('edicao.txtPesquisa')
    searchInAllPapers    = driver.find_element_by_id('chk_avancada_0')
    startDate                  = driver.find_element_by_name('edicao.dtInicio')
    endDate                     = driver.find_element_by_id('dt_fim_avancada')
    submitButton                 = driver.find_element_by_id('pesquisa02_0')
    return  searchString, searchInAllPapers, startDate, endDate, submitButton)


def loadData():
    userInput = input('\033[1;32;40m --> Pressione <ENTER> para buscar por data.json\nOu digite o termo de busca: ')
    return userInput


def setOptions  searchString, searchInAllPapers, startDate):
    searchString.send_keys(loadData())
    searchInAllPapers.click()

    startDate.send_keys(Keys.BACKSPACE)
    startDate.send_keys(Keys.BACKSPACE)
    startDate.send_keys(Keys.BACKSPACE)
    startDate.send_keys(Keys.BACKSPACE)
    startDate.send_keys(Keys.BACKSPACE)

    startDate.send_keys(0)
    startDate.send_keys(1)
    startDate.send_keys(0)
    startDate.send_keys(1)


def submit(submitButton):
    print('\n\033[1;33;40m  --> Submetendo')
    submitButton.click()


presentation()
driver = initialize()   searchString, searchInAllPapers, startDate, endDate, submitButton = connect(
    driver)
setOptions  searchString, searchInAllPapers, startDate)
submit(submitButton)


print('  --> Processando')
allLinks = driver.find_elements_by_class_name('titulo_jornal')
print('\033[1;33;40m---------------------------------------------------------\033[1;32;40m\n')
print('    ', len(allLinks), ' registro(s) encontrado(s):\n')
for link in allLinks:
    print('   ', link.get_attribute('text'))
    print('     >>>', link.get_attribute('href'), '\n')
    print(
        '\033[1;33;40m---------------------------------------------------------\033[1;32;40m')
print('\033[1;33;40m  --> Concluído\n')
driver.quit()
