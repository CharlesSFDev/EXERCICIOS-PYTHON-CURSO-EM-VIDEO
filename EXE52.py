# CÓDIGO QUE RECEBE DO USUÁRIO UM NUMERO INTEIRO E RETORNA SE O MESMO É PRIMOU OU NÃO

numero = int(input('Digite um número para saber se o mesmo é primo: '))

contPrimo = 0

for i in range(1,numero+1):
    if numero % i == 0:
        print('\033[34m', end = ' ')
        contPrimo += 1
    else:
        print('\033[m', end = ' ')
    print('{}'.format(i), end =' ')

print('\nO número {} foi divisível {} vezes.'.format(numero, contPrimo))
if contPrimo == 2:
    print('O número {} é primo!'.format(numero))
else:
    print('O número {} não é primo!'.format(numero))