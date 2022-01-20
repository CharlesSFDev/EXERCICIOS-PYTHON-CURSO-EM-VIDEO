# CÓDIGO QUE COMPARA 2 NÚMEROS E RETORNA QUAL O MAIOR, O MENOR OU SE SÃO IGUAIS

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
  print('O maior número é {}, e o menor é {}.'.format(num1,num2))
elif num2 > num1:
  print('O maior número é {}, e o menor é {}.'.format(num2,num1))
else:
  print('Os 2 números são iguais!!')
