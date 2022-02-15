# CÓDIGO QUE RECEBE DO USUÁRIO VÁRIOS NÚMEROS INTEIROS ATÉ O NÚMERO 999 SER DIGITADO
# AO FINAL A QUANTIDADE DE NÚMEROS DIGITADOS,E SUA SOMA TOTAL, DEVE SER MOSTRADA. O NÚMERO 999 NÃO ENTRA NAS ESTATÍSTICAS

numero = int(input('Digite um número inteiro qualquer: '))

cont = 0
soma = 0
if numero != 999:
    cont = 1
    soma = soma + numero
    while numero != 999:
        numero = int(input('Digite outro número: '))
        if numero != 999:
            cont+=1
            soma = soma+numero

print('Você digitou um total de {} números, e a soma entre eles é: {}.'.format(cont,soma))

