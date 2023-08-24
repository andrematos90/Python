num1=num2=res=0 #variáveis de escopo global

def cn():
    global imprime #desta maneira está variável se torna global e pode ser acessada em todo o código!
    imprime =  "Hello Word!"
    print(imprime)

cn()


""" váriaveis declaradas dentro de uma função tem escopo local e não podem 
ser usadas em outras partes do  código a menos que a palavra  chave "global" seja usada antes do nome da variável"""