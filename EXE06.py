#CÓDIGO QUE RECEBE UM NÚMERO DIGITADO PELO USUÁRIO E RETORNA SEU DUPLO, SEU TRIPLO E SUA RAIZ QUADRADA

numero = float(input('Digite um número: '))

duplo = numero*2
triplo = numero*3
raizQ = numero**(1/2)

print('O número digitado pelo usuário foi: {}.\n Seu dobro é {}, seu triplo é {}, e sua raiz quadrada é {}.'.format(numero,duplo,triplo,raizQ))