# CÓDIGO QUE RECEBE DO USUÁRIO UM NÚMERO N INTEIRO QUALQUER E RETORNA OS N PRIMEIROS TERMOS DA SEQUÊNCIA DE FIBONACCI


numero = int(input('Digite um número inteiro qualquer: '))

cont = 0
print('*'*22)
print('SEQUÊNCIA DE FIBONACCI')
print('*'*22)
t1 = 0
t2 = 1
print('{} {} '.format(t1,t2), end = '')
cont = 3
while cont < (numero+1):
    seq = t1 + t2
    print(seq, end = ' ')
    t1 = t2
    t2 = seq
    cont+=1