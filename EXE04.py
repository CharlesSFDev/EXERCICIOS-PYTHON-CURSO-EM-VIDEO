#EXERCÍCIO PARA COLETAR INFORMAÇÕES SOBRE UMA VARIÁVEL

variavel = input('Digite algo: ')

print('O tipo primitivo desta variável é : {}.'.format(type(variavel)))
print('Só tem espaços? {}.'.format(variavel.isspace()))
print('É um número? {}.'.format(variavel.isnumeric()))
print('É alfanumérico? {}.'.format(variavel.isalnum()))
print('É alfabético: {}.'.format(variavel.isalpha()))
print('É decimal? {}.'.format(variavel.isdecimal()))
print('É composto só de letras minúsculas? {}.'.format(variavel.islower()))
print('É composto só de letras maiúsculas? {}.'.format(variavel.isupper()))
print('É um dígito? {}.'.format(variavel.isdigit()))
print('É printável? {}.'.format(variavel.isprintable()))
