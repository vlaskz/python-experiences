import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


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
    print('Bot para Pesquisa ao Diário Oficial da União 2019\n\
        Desenvolvido por Vlaskz(https: // github.com / vlaskz)\n\
            Disponível em https://github.com/vlaskz/python-experiences/autofill\n')


def initialize():
    print(' --> Inicializando')
    firefox_opt = Options()
    firefox_opt.add_argument('--headless')
    driver = webdriver.Firefox()
    return driver


def connect(driver):
    print('  --> Conectando\n')
    driver.get('http://pesquisa.in.gov.br/imprensa/core/start.action')
    searchString = driver.find_element_by_name('edicao.txtPesquisa')
    searchInAllPapers = driver.find_element_by_id('chk_avancada_0')
    startDate = driver.find_element_by_name('edicao.dtInicio')
    endDate = driver.find_element_by_id('dt_fim_avancada')
    submitButton = driver.find_element_by_id('pesquisa02_0')
    return searchString, searchInAllPapers, startDate, endDate, submitButton


def loadJson():
    with open('data.json', 'r') as data:
        return json.load(data)


def loadData():
    userInput = input(
        '  --> Pressione <ENTER> para buscar por data.json\n  ou digite o termo de busca:')
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
    print('  --> Submetendo')
    submitButton.click()


def fetchResults(driver):
    print('  --> Obtendo Resultados')
    while True:
        more_pages = driver.find_elements_by_partial_link_text('Próximo')
        results = driver.find_elements_by_css_selector('a.titulo_jornal')
        for result in results:
            print(result.get_attribute('text').strip(), '\n',
                  result.get_attribute('href').strip(), '\n',)
        if not results:
            print('  --> Nenhum registro encontrado\n')
            quit()
        if not more_pages:
            for result in results:
                print(result.get_attribute('text').rstrip(), '\n')
            break
        more_pages[0].click()


def main():
    presentation()
    driver = initialize()
    searchString, searchInAllPapers, startDate, endDate, submitButton = connect(driver)
    setOptions(searchString, searchInAllPapers, startDate)
    submit(submitButton)
    fetchResults(driver)
    print('--> Concluído\n')
    driver.quit()


if __name__ == "__main__":
    main()
