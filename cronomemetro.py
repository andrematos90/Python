
def tempo():

import time

hora = 0
minuto = 0
segundo = 0

while True:
    print(f'{hora:02d}:{minuto:02d}:{segundo:02d}', end='\r')
    segundo += 1

    if segundo == 60:
        segundo = 0
        minuto += 1

    if minuto == 60:
        minuto = 0
        hora += 1

    sleep(1)


tempo()