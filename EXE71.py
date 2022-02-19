# CÓDIGO QUE RECEBE DO USUÁRIO UM VALOR INTEIRO, REFERENTE AO VALOR DE UM SAQUE
# O PROGRAMA DEVE RETORNAR A QUANTIDADE DE NOTAS DOS SEGUINTES VALORES: R$ 50, R$ 20, R$ 10 E R$ 1

cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
print('*'*26)
print('Bem vindo ao banco da Zoe!')
print('*'*26)
valor = int(input('Digite o valor do saque: '))

cont50 = int(valor/50)

valor20 = valor - (cont50*50)
cont20 = int(valor20/20)

valor10 = valor - (cont20*20) - (cont50*50)
cont10 = int(valor10/10)

valor1 = valor - (cont10*10) - (cont20*20) - (cont50*50)
cont1 = int(valor1/1)

print(f'Total de cédulas de R$ 50,00: {cont50}.')
print(f'Total de cédulas de R$ 20,00: {cont20}.')
print(f'Total de cédulas de R$ 10,00: {cont10}.')
print(f'Total de cédulas de R$ 1,00: {cont1}.')