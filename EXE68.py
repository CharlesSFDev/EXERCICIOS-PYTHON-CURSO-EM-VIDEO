# CÓDIGO DO JOGO DE PAR OU ÍMPAR ENTRE O COMPUTADOR E O USUÁRIO

from random import randint
contVit = contEmp = 0
while True:
    opcao = str(input('\nVocê quer par ou ímpar? (P/I) ')).strip().upper()[0]
    if opcao.upper() == 'P' or opcao.upper() == 'I':
        entradaUser = int(input('Qual seu número? '))
        entradaPc = randint(0,10)
        somaRodada = entradaPc + entradaUser
        print(f'Você jogou {entradaUser} e o computador jogou {entradaPc}. Resultado da rodada: {somaRodada}')
        if (somaRodada %2 == 0) and (opcao.upper() == 'P'):
            print('Você venceu!!')
            contVit+=1
        elif (somaRodada %2 == 0) and (opcao.upper() == 'I'):
            break
        elif (somaRodada % 2 != 0) and (opcao.upper() == 'I'):
            print('Você venceu!!')
            contVit+=1
        elif (somaRodada == 0):
            print('Deu empate.')
            contEmp+=1
        else:
            break
        somaRodada = 0
    else:
        print('Opção inválida.')
print('\nO Computador venceu esta rodada.')
print(f'Você venceu {contVit} rodadas consecutivas.')



