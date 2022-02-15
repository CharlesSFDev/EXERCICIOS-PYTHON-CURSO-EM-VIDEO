# CÓDIGO QUE RECEBE DO USUÁRIO 1 NÚMERO INTEIRO QUALQUER E RETORNA SEU FATORIAL

from math import factorial

numero = int(input('Digite um número inteiro para o cálculo de seu fatorial: '))

cont = numero
fat = 1

while cont > 0:

    fat *= cont
    cont-=1

print('O fatorial de {} é {}.'.format(numero,fat))
