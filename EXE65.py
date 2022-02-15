# CÓDIGO QUE RECEBE DO USUÁRIO VÁRIOS NÚMEROS INTEIROS, E AO FINAL RETORNA A MÉDIA ENTRE ELES, O MAIOR VALOR
# E O MENOR VALOR. O USUÁRIO DECIDE SE QUER CONTINUAR DIGITANDO NÚMEROS OU NÃO


entrada = int(input('Digite um número inteiro qualquer: '))
cont = 0
soma = 0
soma = soma + entrada
maior = 0
menor = 1000000
resp = False
while not resp:
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada
    perg = str(input('Deseja continuar digitando números (S/N): '))
    if perg.upper() == 'S':
        entrada = int(input('Digite um número inteiro qualquer: '))
        soma += entrada
    elif perg.upper() == 'N':
        resp = True
    else:
        print('Entrada inválida!!')
        cont-=1
    cont += 1

media = soma/cont

print('Ao total, você digitou {} números. A média entre eles foi: {}.'.format(cont,media))
print('\nO maior número digitado foi {}, e o menor foi {}.'.format(maior, menor))