# CÓDIGO QUE RECEBE DO USUÁRIO 1 NÚMERO INTEIRO, CALCULA E MOSTRA SUA TABUADA NA TELA

numero = int(input('Digite um número inteiro para o cálculo de sua tabuada: '))

print('TABUADA DO NÚMERO {}'.format(numero))
for i in range(1,11,1):
    print('{} x {} = {}'.format(i,numero,i*numero))

