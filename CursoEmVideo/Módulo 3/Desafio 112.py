'''112 - Dentro do pacote, no módulo dado. Crie uma função chamda leiaDinheiro().
 Que seja capaz de funcionar como um input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''
from pacotes import dados

v = dados.leiaDinheiro('Valor R$: ')
dados.resumo(v)            