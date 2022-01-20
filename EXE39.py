#CÓDIGO QUE RECEBE DO USUÁRIO O ANO DE NASCIMENTO E CALCULA O TEMPO DE ALISTAMENTO

ano = int(input('Digite seu ano de nascimento: '))

anoAtual = 2021

if (anoAtual - ano) == 18:
  print('Você deve se alistar esse ano!')
elif (anoAtual - ano) < 18:
  print('Você não precisa se alistar agora. Seu ano de alistamento é {}.'.format(anoAtual+(18-(anoAtual-ano))))
else:
  print('Você já passou do tempo de se alistar. Deveria ter se alistado em {}.'.format(anoAtual-((anoAtual-ano-18))))
