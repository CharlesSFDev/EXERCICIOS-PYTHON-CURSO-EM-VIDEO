# CÓDIGO QUE RECEBE DO USUÁRIO QUALQUER NÚMERO INTEIRO POSITIVO E RETORNA SUA TABUADA
# QUANDO O USUÁRIO DIGITAR UM NÚMERO NEGATIVO, O CÓDIGO PARA A EXECUÇÃO

while True:
    numero = int(input('Digite um número inteiro para o cálculo da tabuada (para sair, digite um número negativo): '))
    if numero < 0:
        break
    print('*'*50)
    for i in range(1,11):
        print(f'{i} x {numero} = {i*numero}')
        i+=1
    print('*'*50)