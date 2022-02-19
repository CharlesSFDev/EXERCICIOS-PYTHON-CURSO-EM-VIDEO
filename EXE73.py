# CÓDIGO QUE MOSTRA AO USUÁRIO:
# OS 5 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE 2021, SÉRIE A
# OS ÚLTIMOS 4 COLOCADOS DA TABELA
# IMPRIME OS NOMES DOS TIMES EM ORDEM ALFABÉTICA
# MOSTRA A COLOCAÇÃO DA CHAPECOENSE NA TABELA

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
          'Atletico-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
          'Bahia', 'Sport', 'Chapecoense')

print('*'*26)
print('CAMPEONATO BRASILEIRO 2021')
print('*'*26)

print('\nOs 5 primeiros colocados são:')
print(tabela[0:5])

#for pos, time in enumerate(tabela):
#    if pos <= 4:
#        print(f'{pos+1} - {time}')
#        pos+=1

print('\nOs 4 últimos colocados são:')
print(tabela[-4:])

#for pos, time in enumerate(tabela):
#    if pos >= 16:
#        print(f'{pos+1} - {time}')

print('\nTimes em ordem alfabética:')
print(sorted(tabela))


print('\nPosição da Chapecoense:')
print(f'A chapecoense está na posição {tabela.index("Chapecoense")+1}')

#for pos, time in enumerate(tabela):
#    if time == 'Chapecoense':
#        print(f'A {time} está na {pos+1}ª posição.')