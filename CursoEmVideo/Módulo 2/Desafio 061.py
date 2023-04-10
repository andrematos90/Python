'''Refaça o exercicio 051, lendo o primeiro de uma PA e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura da while.'''

'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

primeiro_termo = int(input('Digite o primeiro da PA: '))
razão = int(input('Digite o termo da razão: '))

for c in range(primeiro_termo, razão * 10, razão):
    termo = primeiro_termo + (c - 1) * razão
    print(c, c + 1)
    


    # formula para calcular o enésimo 
    #  termo = primeiro_termo + (i - 1) * razao
    

