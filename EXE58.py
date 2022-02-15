# CÓDIGO QUE RECEBE DO USUÁRIO UM NÚMERO ENTRE 0 E 10 E COMPARA COM UM NÚMERO RANDÔMICO GERADO PELO COMPUTADOR
# CASO O USUÁRIO ACERTE, O COMPUTADOR RETORNA A QUANTIDADE DE VEZES QUE O USUÁRIO LEVOU ATÉ ACERTAR O NÚMERO

from random import randint

numero = randint(0,10)

entrada = int(input('Tente acertar qual o número (entre 0 e 10): '))

contador = 1
while entrada != numero:
    entrada = int(input('Tente acertar qual o número (entre 0 e 10): '))
    contador+=1

print('VOCÊ ACERTOU!! O número era {}.'.format(numero))
print('Você precisou de {} tentativas para acertar o número.'.format(contador))

# RESPOSTA ALTERNATIVA
'''
acertou = False
while not acertou:
    entrada = int(input('Tente acertar qual o número (entre 0 e 10): '))
    contador+=1
    if numero == entrada:
        acertou = True

print('VOCÊ ACERTOU!! O número era {}.'.format(numero))
print('Você precisou de {} tentativas para acertar o número.'.format(contador))
'''