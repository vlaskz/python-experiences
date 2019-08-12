from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

# ciclo do programa:
# mostrar texto de apresentação - OK
# inicializar o driver - OK
# conectar ao site e obter os objetos - OK
# carregar os dados do prompt ou do data.json - IN PROCESS
# se for via prompt, executar e sair - OK
# se for via data.json, fazer uma pesquisa para cada registro - IN PROCESS
# exibir os registros encontrados - OK
# sair


def presentation():
    print('\033[H\033[J\033[1;34;40m')
    print('Bot para Pesquisa ao Diário Oficial da União 2019\n\
        Desenvolvido por Vlaskz(https: // github.com / vlaskz)\n\
            Disponível em https://github.com/vlaskz/python-experiences/autofill\n')


def initialize():
    print('\033[1;33;40m', ' --> Inicializando')
    chrome_opt = Options()
    chrome_opt.add_argument('--headless')
    webDriver = webdriver.Chrome('C:\\sel\\chromedriver.exe', 0, chrome_opt)
    return webDriver


def connect(webDriver):
    print('  --> Conectando\n')
    webDriver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')
    searchString = webDriver.find_element_by_name('edicao.txtPesquisa')
    searchInAllPapers = webDriver.find_element_by_id('chk_avancada_0')
    startDate = webDriver.find_element_by_name('edicao.dtInicio')
    endDate = webDriver.find_element_by_id('dt_fim_avancada')
    submitButton = webDriver.find_element_by_id('pesquisa02_0')
    return searchString, searchInAllPapers, startDate, endDate, submitButton


def loadJson():
    with open('data.json', 'r') as data:
        return json.load(data)


def loadData():
    userInput = input(
        '  --> Pressione <ENTER> para buscar por data.json\n  ou digite o termo de busca:\033[1;36;40m ')
    if not userInput or userInput.strip() == '':
        userInput = loadJson()
        print(json.dumps(userInput, indent=4, sort_keys=True))
        quit()

    return userInput


def setOptions(searchString, searchInAllPapers, startDate):
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
    print('\n\033[1;33;40m', '  --> Submetendo')
    submitButton.click()


def fetchResults(webDriver):
    print('  --> Obtendo Resultados')
    results = []
    while True:
        morePages = webDriver.find_elements_by_partial_link_text('Próximo')
        results = webDriver.find_elements_by_css_selector('a.titulo_jornal')
        for result in results:
            print('\n\033[1;32;40m', result.get_attribute('text').strip(), '\n',
                  result.get_attribute('href').strip(), '\n',)
        if not results:
            print('\n\033[1;31;40m', '  --> Nenhum registro encontrado\n')
            quit()
        if not morePages:
            for result in results:
                print(result.get_attribute('text').rstrip(), '\n')
            break
        morePages[0].click()


def main():
    presentation()
    webDriver = initialize()
    searchString, searchInAllPapers, startDate, endDate, submitButton = connect(
        webDriver)
    setOptions(searchString, searchInAllPapers, startDate)
    submit(submitButton)
    fetchResults(webDriver)
    print('\033[1;33;40m  --> Concluído\n')
    webDriver.quit()


if __name__ == "__main__":
    main()
