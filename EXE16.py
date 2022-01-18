#CÓDIGO QUE RECEBE DO USUÁRIO UM NÚMERO REAL DECIMA E IMPRIME APENAS A PARTE INTEIRA DO MESMO

import math

num = float(input('Digite um número qualquer: '))

inteiro = math.trunc(num)

print('A parte inteira do número {} é: {}.'.format(num,inteiro))
