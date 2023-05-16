import pyautogui
from time import sleep
import pandas as pa
'''
pyautogui.click (clica em algum local da tela)
pyautogui.write (escreve texto)
pyautogui.press (pressiona uma tecla)
pyautogui.hotkey(pressiona uma combinação de tecla)
'''

#Acessar o sistema da empresa
pyautogui.PAUSE = 2
pyautogui.hotkey('win')
pyautogui.write('chrome')
sleep(5)
pyautogui.press('Enter')
pyautogui.write(r'https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('Enter')
sleep(3)

#Fazer Login no Sistema
pyautogui.click(x=584, y=337)
pyautogui.write('Admin')
pyautogui.click(x=542, y=419)
pyautogui.write('senha')
pyautogui.click(x=644, y=482)
sleep(5)

#Baixar base de dados
pyautogui.rightClick(x=374, y=312)
sleep(5)
pyautogui.click(x=461, y=574)
sleep(5)

#Calcular Indicadores
#importar base de dados 
tabela = pa.read_csv(r'C:\Users\andre\OneDrive\Documentos\GitHub\Python\Intensivão de Python\arquivos\Compras.csv', sep=';')
#cálculo dos indicadores
#total
total_gasto = tabela['ValorFinal'].sum()
#quantidade, 
quantidade = tabela['Quantidade'].sum()
#preço médio
preco_medio = total_gasto / quantidade
#Enviar E-email
#entrar no e-mail
pyautogui.click(x=456, y=52)
sleep(2)
pyautogui.write('https://mail.google.com/mail/u/0/?pli=1#inbox')
sleep(2)
pyautogui.press('Enter')
#clicar em escrever
pyautogui.click(x=265, y=424)
sleep(2)
pyautogui.write('andrejlle76@gmail.com')
sleep(2)
pyautogui.press('Enter')
pyautogui.click(x=826, y=339)
pyautogui.write('Relatório')
#preencher e e-mail
#enviar