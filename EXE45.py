# CÓDIGO QUE FAZ O COMPUTADOR JOGAR JOKENPÔ COM O USUÁRIO "PEDRA, PAPEL E TESOURA"

import random

pcChoices = ['PEDRA', 'PAPEL', 'TESOURA']

pcSort = random.randint(0,2)

print('*******')
print('JOKENPÔ')
print('*******')

print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')

humanChoice = int(input('Escolha uma das alternativas: '))

if (humanChoice == 1) and (pcSort == 0):
  print('O JOGO DEU EMPATE.')
  print('Minha escolha foi {}, e a sua foi PEDRA.'.format(pcChoices[pcSort]))
elif (humanChoice == 1) and (pcSort == 1):
  print('EU GANHEI!!')
  print('Minha escolha foi {}, e a sua foi PEDRA. {} embrulha PEDRA!'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 1) and (pcSort == 2):
  print('VOCÊ GANHOU!!')
  print('Minha escolha foi {}, e a sua foi PEDRA. PEDRA quebra {}.'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 2) and (pcSort == 0):
  print('VOCÊ GANHOU!!')
  print('Minha escolha foi {}, e a sua foi PAPEL. PAPEL embrulha {}.'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 2) and (pcSort == 1):
  print('O JOGO DEU EMPATE.!!')
  print('Minha escolha foi {}, e a sua foi PAPEL.'.format(pcChoices[pcSort]))
elif (humanChoice == 2) and (pcSort == 2):
  print('EU GANHEI!!')
  print('Minha escolha foi {}, e a sua foi PAPEL. {} corta PAPEL.'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 3) and (pcSort == 0):
  print('EU GANHEI!!')
  print('Minha escolha foi {}, e a sua foi TESOURA. {} quebra TESOURA.'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 3) and (pcSort == 1):
  print('VOCÊ GANHOU!!')
  print('Minha escolha foi {}, e a sua foi TESOURA. TESOURA corta {}.'.format(pcChoices[pcSort],pcChoices[pcSort]))
elif (humanChoice == 3) and (pcSort == 2):
  print('O JOGO DEU EMPATE.')
  print('Minha escolha foi {}, e a sua foi TESOURA.'.format(pcChoices[pcSort]))
else:
  print('JOGADA INVÁLIDA!!')
