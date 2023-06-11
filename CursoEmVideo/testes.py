import time
import sys
from msvcrt import kbhit

def cronometro():
    inicio = time.time()
    while not kbhit():
        tempo_passado = time.time() - inicio
        minutos, segundos = divmod(tempo_passado, 60)
        tempo_formatado = f'{int(minutos):02d}:{int(segundos):02d}'
        print(tempo_formatado, end='\r')
        time.sleep(0.1)
    sys.stdin.read(1)  # Descarta a tecla pressionada

# Exemplo de uso do cronômetro
print("Pressione qualquer tecla para parar o cronômetro.")
cronometro()
print("Cronômetro parado!")

   
