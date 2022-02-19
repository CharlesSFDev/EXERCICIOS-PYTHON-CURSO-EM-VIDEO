# CÓDIGO QUE RECEBE DO USUÁRIO VÁRIOS NÚMEROS INTEIROS ATÉ O NÚMERO 999 SER DIGITADO
# AO FINAL A QUANTIDADE DE NÚMEROS DIGITADOS,E SUA SOMA TOTAL, DEVE SER MOSTRADA. O NÚMERO 999 NÃO ENTRA NAS ESTATÍSTICAS

numero = 0
cont = 0
soma = 0
while True:
    numero = int(input('Digite um número qualquer: (999 para parar) '))
    if numero == 999:
        break
    cont+=1
    soma+=numero

print(f'Você digitou um total de {cont} números, e a soma deles foi {soma}.')
