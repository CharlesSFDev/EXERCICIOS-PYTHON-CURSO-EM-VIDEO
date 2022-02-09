# CÓDIGO QUE RECEBE O PESO DE 5 PESSOAS E RETORNA O MAIOR E O MENOR ENTRE ELES

maior = 0
menor = 200

for i in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso digitado foi {}, e o menor foi {}.'.format(maior, menor))