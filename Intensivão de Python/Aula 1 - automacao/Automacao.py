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
pyautogui.click(x=1893, y=415)
pyautogui.write('Admin')
pyautogui.click(x=1895, y=485)
pyautogui.write('senha')
pyautogui.click(x=1973, y=559)
sleep(5)

#Baixar base Relatrio dados
pyautogui.rightClick(x=1717, y=391)
sleep(5)
pyautogui.click(x=1841, y=592)
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
pyautogui.click(x=1812, y=128)
sleep(2)
pyautogui.write('https://mail.google.com/mail/u/0/?pli=1#inbox')
sleep(2)
pyautogui.press('Enter')
sleep(2)
#clicar em escrever
pyautogui.click(x=1461, y=242)
sleep(2)
pyautogui.write('andrejlle76@gmail.com')
sleep(2)
pyautogui.press('Enter')
pyautogui.click(x=2136, y=373)
pyautogui.write('Relatório')
#preencher e e-mailchrome
#enviarAdminAdmin