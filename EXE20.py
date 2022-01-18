#CÓDIGO QUE RECEBE 4 NOMES DE ALUNOS E FAZ O SORTEIO DA ORDEM DE APRESENTAÇÃO ALEATORIAMENTE

import random

alunos = ['','','','']

cont = 0

while cont < 4:
    alunos[cont] = input('Escreva o nome do aluno: ')
    cont+=1

alunosSort = random.sample(alunos,len(alunos))

print('ORDEM DE APRESENTAÇÃO!')

contSort = 0

for i in alunosSort:
    print('{} será o {} a apresentar.'.format(i,(contSort+1)))
    contSort+=1