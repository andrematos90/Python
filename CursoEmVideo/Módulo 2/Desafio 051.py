'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

# Lê o primeiro termo e a razão da Progressão Aritmética
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Calcula e imprime os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são: ")
for i in range(1, 11):
    termo = primeiro_termo + (i - 1) * razao
    print("{}".format(termo))

    # formula para calcular o enésimo 
    #  termo = primeiro_termo + (i - 1) * razao


'''
primeiro_termo = int(input('Primeiro termo da progressão: '))
razao = int(input('Razão da progressão: '))

for c in range(primeiro_termo, primeiro_termo + 10, razao):
    print(c)'''