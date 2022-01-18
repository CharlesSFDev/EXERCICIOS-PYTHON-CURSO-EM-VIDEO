# CÓDIGO QUE RECEBE DO USUÁRIO UM NOME COMPLETO E RETORNA SEU PRIMEIRO E SEU ÚLTIMO NOMES

nome = str(input('Digite o nome completo: ')).strip()

n = nome.split()

print('Primeiro nome = {}.'.format(n[0]))
print('Último nome = {}.'.format(n[len(n)-1]))