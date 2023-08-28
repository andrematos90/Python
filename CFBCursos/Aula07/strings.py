string = "André Rosa de Matos" 

res = "André" in string
print(res) # operador "in" verifica se existe o que foi pedido na string e retorn true ou false

resnot = "André" not in string
print(resnot) # not in nega, inverte o resultado da verificação

cidade = "Joinville"
dia = 28
mes = "Agosto"
ano = 2023

#formas de imprimir

#concatenação
print("Cidade de " + cidade + ", dia " + str(dia) + " de " + mes + " do ano de " + str(ano))

#Método % (antigo):
print("Cidade de %s, dia %d mes de %a do ano de %s" % (cidade, dia, mes, ano))


#Método .format():
print("Cidade de {}, dia {} mes {} do ano de {}".format(cidade, dia, mes, ano))

#F-strings (a partir do Python 3.6):
print(f"Cidade de {cidade}, dia {dia} mes {mes} do ano de {ano}")

#Método str.join():
palavras = ["Olá", "mundo", "!"]
mensagem = " ".join(palavras)
print(mensagem)


#Formatação múltipla: Se você deseja repetir o mesmo valor em vários lugares da string, você #pode usar formatação múltipla para inserir o mesmo valor em vários espaços reservados.
nome = "André"
saudacao = f"Olá, {nome}! Como vai, {nome}?"
print(saudacao)

#Função print() com múltiplos argumentos:
#A função print() em Python pode receber múltiplos argumentos separados por vírgula. Ela #imprimirá os argumentos separados por um espaço padrão.

nome = "André"
idade = 33
print("Olá,", nome, "você tem", idade, "anos.") 
