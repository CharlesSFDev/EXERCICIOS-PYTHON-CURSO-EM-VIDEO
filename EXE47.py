# CÓDIGO QUE CONTA DE 1 ATÉ 50 E IMPRIME NA TELA TODOS OS NÚMEROS PARES NESTE INTERVALO

for i in range(2,51,2):
    if i %2 == 0:
        print('{}'.format(i), end = ' ')