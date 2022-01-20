# CÓDIGO QUE CALCULA A MÉDIA DE 3 NOTAS E RETORNA A SITUAÇÃO DO ALUNO DEPENDENDO DA MÉDIA

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media = (nota1+nota2+nota3)/3

print('Média = {}.'.format(media))
if media < 5:
  print('Você está reprovado.')
elif media >= 5 and media < 7:
  print('Você está em recuperação.')
elif media >= 7 and media <= 10:
  print('Parabéns, você foi APROVADO!')
else:
    print('Média e notas fora do padrão.')