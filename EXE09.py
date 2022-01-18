#CÓDIGO QUE RECECE UM NÚMERO DO USUÁRIO E RETORNA SUA TABUADA

numero = int(input('Digite um número inteiro entre 0 e 9: '))

print('TABUADA')

contador = 0

while contador < 11:
    print('{}   X   {}  =  {}'.format(numero,contador,(numero*contador)))
    contador+=1