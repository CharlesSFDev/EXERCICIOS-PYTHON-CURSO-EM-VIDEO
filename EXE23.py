#CÓDIGO QUE RECEBE DO USUÁRIO UM NUMERO ENTRE 0 E 9999 E RETORNA SUA UNIDADE, SUA DEZENA, SUA CENTENA E SEU MILHAR

numero = int(input('Digite um número entre 0 e 9999: '))

u = numero // 1%10
d = numero // 10%10
c = numero // 100%10
m = numero // 1000%10

print('Unidade = {}, dezena = {}, centena = {}, milhar = {}.'.format(u,d,c,m))
