#1PASSO: ABRIR NAVEGADOR
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://www.google.com/webhp?hl=pt-BR&sa=X&ved=0ahUKEwju1NXe6P7-AhUlAbkGHbXYCiMQPAgI')

#2PASSO: IMPORTAR BASE DE DADOS
import pandas as pd

tabela = pd.read_excel(r'C:\Users\andre\OneDrive\Documentos\GitHub\Python\Intensivão de Python\Aula 3 - automacao web\commodities.xlsx')

#3PASSO: ENTRAR NO SITE DE CAMBIO,SELECIONAR CAMPO, PEGAR VALOR E JOGAR NA TABELA
for linha in tabela.index:
    produto = tabela.loc[linha, 'Produto']
    link = f'https://www.melhorcambio.com/{produto}-hoje'
    link = link.replace('á', 'a').replace('ã', 'a').replace('ó', 'o').replace('é', 'e').replace('ú', 'u').replace('ç', 'c')
    navegador.get(link)
    #selecionar o campo no site através do xpath e pega a cotacao 
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.', '').replace(',','.')
    cotacao = float(cotacao)
    #com o campo selecionado 3 coisas podem ser feitas:
    #.send_keys('esvrever no campo)
    #.click() --> clicar no campo
    #.get_atribute() --> pega o valor do campo 

    #4PASSO: PREENCHER TABELA COM PREÇO ATUAL
    tabela.loc[linha, 'Preço Atual'] = cotacao
print(tabela)

#4PASSO: PREENCHER SE DEVE OU NÃO COMPRAR
#verifica para cada linha se o preço atual é menor que o preço ideal se sim coluna "comprar recebe "true"
tabela['Comprar'] = tabela['Preço Atual'] < tabela['Preço Ideal']


#5PASSO EXPORTAR PARA EXCEL
#fecha o navegador
navegador.quit()
#exporta
tabela.to_excel('commodities_atualizado.xlsx')