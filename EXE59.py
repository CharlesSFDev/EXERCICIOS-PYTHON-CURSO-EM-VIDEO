# CÓDIGO QUE RECEBE DO USUÁRIO 2 NÚMEROS E DÁ OPÇÕES PARA SOMA, MULTIPLICAÇÃO, MAIOR E MENOR
# A OPÇÃO DE SAIR DO PROGRAMA TAMBÉM DEVE EXISTIR, E SEMPRE QUE UMA OPÇÃO FOR DIGITADA, O COMPUTADOR DEVE MOSTRAR A RESPOSTA

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

sair = False

while not sair:
    print('\nTemos 5 opções para você.')
    print('\n1 - MOSTRAR A SOMA ENTRE OS NÚMEROS'
          '\n2 - MOSTRAR A MULTIPLICAÇÃO ENTRE OS NÚMEROS'
          '\n3 - MAIOR NÚMERO DIGITADO'
          '\n4 - RECEBER NOVOS NÚMEROS'
          '\n5 - SAIR DO PROGRAMA')

    opcao = int(input('\nDigite uma opção: '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre os números {} e {} é: {}.'.format(num1,num2,soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação entre os números {} e {} é: {}.'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('O maior número entre {} e {} é: {}.'.format(num1, num2, maior))
        elif num2 > num1:
            maior = num2
            print('O maior número entre {} e {} é: {}.'.format(num1, num2, maior))
        else:
            print('Os números {} e {} são iguais.'.format(num1, num2))
    elif opcao == 4:
        print('Informe 2 novos números.')
        num1 = int(input('Digite o novo primeiro número: '))
        num2 = int(input('Digite o novo segundo número: '))
        print('Os novos números são {} e {}.'.format(num1, num2))
    elif opcao == 5:
        print('Parando execução do programa!')
        sair = True
    else:
        print('Opção inválida. Tente novamente.')