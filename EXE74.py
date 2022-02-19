# CÓDIGO QUE GERA 5 NÚMEROS ALEATÓRIOS E O COLOCAM DENTRO DE UMA TUPLA
# APÓS ISTO, O CÓDIGO DEVE IMPRIMIR ESTES 5 NÚMEROS E MOSTRAR QUAL O MAIOR E QUAL O MENOR ENTRE ELES

from random import randint

nums = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print('TUPLA GERADA RANDOMICAMENTE:')
print(nums, end = ' ')

maior = nums[0]
menor = nums[0]

for i in nums:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'\nO maior número da tupla é {maior}, e o menor número é {menor}')