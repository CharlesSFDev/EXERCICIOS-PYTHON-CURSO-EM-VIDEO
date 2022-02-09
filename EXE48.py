# CÓDIGO QUE FAZ A SOMA DE TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE 3 NO INTERVALO DE 1 ATÉ 500

soma = 0
for i in range(1,500,2):
    if i %3 == 0:
        soma = soma + i

print('A soma total de todos os números ímpares múltiplos de 3 no intervalo de 1 até 500 é {}'.format(soma))