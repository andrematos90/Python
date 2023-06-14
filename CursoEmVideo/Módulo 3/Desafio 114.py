'''114 - Crie um código em python que teste se o site Pudim.com.br está acessivel pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não está acessível!')
else:
    print('site conectado!')

'''
import urllib: Importa o módulo urllib, que é uma biblioteca padrão do Python usada para trabalhar com URLs.

import urllib.request: Importa a submódulo request da biblioteca urllib, que contém funções para abrir URLs.

try:: Inicia um bloco de código onde exceções serão tratadas.

site = urllib.request.urlopen('http://www.pudim.com.br'): Usa a função urlopen do módulo urllib.request para abrir a URL "http://www.pudim.com.br" e atribui o resultado à variável site. Essa função retorna um objeto de resposta que representa a página da web.

except urllib.error.URLError:: Se ocorrer um erro do tipo URLError durante a execução do bloco de código anterior, o fluxo do programa é redirecionado para este bloco. O URLError é uma exceção específica do módulo urllib.error que é lançada quando ocorre um erro ao abrir uma URL.

print('Site não está acessível!'): Se a exceção URLError for capturada, esta linha será executada e imprime a mensagem "Site não está acessível!".

else:: Se nenhuma exceção for lançada durante a execução do bloco de código no ponto 4, o fluxo do programa é redirecionado para este bloco.

print('site conectado!'): Se nenhum erro ocorrer, esta linha será executada e imprime a mensagem "site conectado!".

Basicamente, o código tenta abrir a URL "http://www.pudim.com.br" usando urlopen. Se a URL for acessível, a mensagem "site conectado!" será impressa. Caso contrário, se ocorrer um erro durante a tentativa de acesso à URL, a mensagem "Site não está acessível!" será exibida.






'''