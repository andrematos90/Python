'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

# Lê o primeiro termo e a razão da Progressão Aritmética
primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

# Calcula e imprime os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são: ")
for i in range(1, 11):
    termo = primeiro_termo + (i - 1) * razao
    print("{:.2f}".format(termo))