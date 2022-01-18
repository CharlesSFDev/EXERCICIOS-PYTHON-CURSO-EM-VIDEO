# CÓDIGO QUE FAZ COM QUE 1 NÚMERO SEJA GERADO ALEATORIAMENTE (ENTRE 0 E 5), AFIM DE SABER SE O USUÁRIO ADIVINHA-O OU NÃO

import random


numero = random.randint(0,5)

print('*************************')
print('   JOGO DA ADIVINHAÇÃO   ')
print('*************************')

entrada = int(input('Digite um número: '))

print('PROCESSANDO...')

if entrada == numero:
    print('PARABÉNS, VOCÊ ACERTOU!!')
else:
    print('Você errou. \nNúmero sorteado: {}\nNúmero digitado: {}.'.format(numero,entrada))
