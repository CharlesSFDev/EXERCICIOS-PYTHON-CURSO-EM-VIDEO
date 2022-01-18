#CÓDIGO QUE RECEBE DO USUÁRIO UM NOME COMPLETO E RETORNA O MESMO EM MAIUSCULO, MINUSCULO, A QTDE TOTAL DE LETRAS E A QTDE DE LETRAS DO PRIMEIRO NOME

nome = str(input("Digite seu nome completo: "))

print('Seu nome todo em maiúsculo: {}.'.format(nome.upper()))
print('Seu nome todo em minúsculo: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))