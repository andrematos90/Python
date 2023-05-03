# algoritimo para ler um preço de produto e mostrar esse preço com 5% de desconto

preco = float(input('Digite o Preço do produto: '))
porcentagem = preco/100
novopreco = preco-(porcentagem*5)
print('Preço com desconto: {}'.format(novopreco))

'''
outra forma 

algoritimo para ler um preço de produto e mostrar esse preço com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desconto = (preco / 100 ) * 5

print(f'Valor com desconto: {preco - desconto:.2f}')'''

