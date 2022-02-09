# CÓDIGO QUE RECEBE DO USUÁRIO 6 NÚMEROS INTEIROS E MOSTRA A SOMA DOS NÚMEROS PARES DIGITADOS

soma = 0

for i in range(0,6,1):
    numero = int(input('Digite o {}º número: '.format(i+1)))
    if numero %2 == 0:
        soma = soma + numero

print('A soma de todos os números pares digitados é {}.'.format(soma))

