#CÓDIGO QUE RECEBE DO USUÁRIO O NOME COMPLETO E VERIFICA SE CONTÉM "SILVA" NO NOME

nome = str(input('Digite o nome completo: ')).strip()

print('O nome tem Silva? {}.'.format('SILVA' in nome.upper()))


