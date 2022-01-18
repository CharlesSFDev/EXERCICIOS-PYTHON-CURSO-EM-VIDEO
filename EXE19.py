#CÓDIGO QUE RECEBE 4 NOMES DE ALUNOS E SORTEIA 1 ALEATORIAMENTE

import random

alunos = ['','','','']

cont = 0

while cont < 4:
    alunos[cont] = input('Escreva o nome do aluno: ')
    cont+=1
sorteio = random.randint(0,3)

print('Dos 4 alunos, o sorteado foi {}. Parabéns!'.format(alunos[sorteio]))