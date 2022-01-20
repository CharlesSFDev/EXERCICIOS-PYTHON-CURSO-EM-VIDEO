# CÓDIGO QUE FAZ A CONVESÃO DO NÚMERO DECIMAL EM BINÁRIO, OCTODECIMAL E HEXADECIMAL, DE ACORDO COM A ESCOLHA DO USUÁRIO

def decToBin(valDec):
  if valDec >= 1:
    decToBin(valDec // 2)
  print(valDec%2, end = ' ')

def decToOcto(valDec):
  if valDec > 0:
    decToOcto((int)(valDec/8))
  print(valDec%8, end = ' ')

conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def decToHex(valDec):
    if(valDec <= 0):
        return ''
    resto = valDec%16
    return  decToHex(valDec // 16)+conversion_table[resto]

num = int(input('Digite um numero decimal e inteiro: '))

print('Em qual base você deseja converter o número?\n1 - Binário\n2 - Octo\n3 - Hexadecimal')

entrada = int(input())

if entrada == 1:
  decToBin(num)
  print('\n')
elif entrada == 2:
  decToOcto(num)
  print('\n')
elif entrada == 3:
  print(decToHex(num))
  print('\n')
else:
  print('Operação inválida!')
