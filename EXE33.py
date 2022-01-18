# CÓDIGO QUE RECEBE 3 NÚMERO E RETORNA QUAL O MAIOR E QUAL O MENOR

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = 0
menor = 0
if ((num1 > num2) and (num1 > num3)):
    maior = num1
    print('Maior número = {}'.format(maior))
elif ((num2 > num1) and (num2 > num3)):
    maior = num2
    print('Maior número = {}'.format(maior))
elif ((num3 > num1) and (num3 > num2)):
    maior = num3
    print('Maior número = {}'.format(maior))

if ((num1 < num2) and (num1 < num3)):
    menor = num1
    print('Menor número = {}'.format(menor))
elif ((num2 < num1) and (num2 < num3)):
    menor = num2
    print('Menor número = {}'.format(menor))
else:
    menor = num3
    print('Menor número = {}'.format(menor))



