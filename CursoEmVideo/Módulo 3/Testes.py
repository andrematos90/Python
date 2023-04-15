import random

# Criando uma tupla vazia
tupla = ()

# Gerando cinco números aleatórios entre 1 e 100 e adicionando-os à tupla
for i in range(5):
    numero = random.randint(1, 100)
    tupla += (numero,)

# Imprimindo a tupla com os números aleatórios
print(tupla)
