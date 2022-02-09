# CÓDIGO QUE FAZ UMA CONTAGEM REGRESSIVA, DE 10 ATÉ 0, ESPERANDO 1 SEGUNDO DURANTE ESTA CONTAGEM

import time
from time import sleep

print('Contagem regressiva!')

for i in range(10, -1, -1):
    print(i)
    sleep(0.1)

print('FELIZ ANO NOVO!!')