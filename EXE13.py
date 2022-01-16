#CÓDIGO QUE RECEBE UM VALOR DE SALÁRIO E CALCULA SEU NOVO VALOR COM 15% DE AUMENTO

salario = float(input('Digite o valor do salário: '))

aumento = 15/100

novoSalario = salario + (aumento*salario)

print('O salário inicial, com valor de {} reais, passa a ser {} reais, considerando os 15% de aumento'.format(salario,novoSalario))