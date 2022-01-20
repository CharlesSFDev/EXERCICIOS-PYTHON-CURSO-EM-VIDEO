# CÓDIGO QUE RECEBE DO USUÁRIO O ANO DE NASCIMENTO DE UM ATLETA E RETORNA SUA CATEGORIA
# DE ACORDO COM SUA IDADE

ano = int(input('Digite o ano de nascimento do atleta: '))

anoAtual = 2021

idade = anoAtual - ano

if idade < 9:
  print('Atleta da categoria Mirim.')
elif idade >=9 and idade < 14:
  print('Atleta da categoria Infantil.')
elif idade >= 14 and idade < 19:
  print('Atleta da categoria Júnior.')
elif idade >= 19 and idade < 25:
  print('Atleta da categoria Sênior.')
else:
  print('Atleta da categoria Master.')
