try:

    a = int(input('\033[0;32mDenominador: \033[m'))
    b = int(input('\033[0;30mDivisor: \033[m'))
    r = a / b

except ZeroDivisionError:
    print('\033[0;31mERRO!Um número não pode ser dividido por 0!\033[0m')

except ValueError:
    print('\33[0;31mERRO! Insira apenas numeros inteiros\033[0m')

except Exception as erro:
    print(f'\033[0;31mERRO! A causa do erro encontrado foi {erro.__cause__}\033[0m')

else:
    print(f'Resultado: {r}')

finally:
    print('\033[0;34mObrigado!\033[0m')

