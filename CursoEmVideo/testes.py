def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a dentro é: {a}')
    print(f'b dentro é: {b}')
    print(f'c dentro é: {c}')

a = 5
teste(a)
print(f'a fora vale: {a}')
  
  
