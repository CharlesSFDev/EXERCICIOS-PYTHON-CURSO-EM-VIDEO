# CÓDIGO QUE RECEBE DO USUÁRIO O PESO E A ALTURA DE UM INDIVÍDUO,CALCULA E RETORNA SEU IMC, JUNTAMENTE
# COM QUAL CATEGORIA DE CLASSIFICAÇÃO DE IMC SE ENCONTRA O INDIVÍDUO EM QUESTÃO

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso/(altura*altura)

print('Seu IMC é {}.'.format(imc))

if imc < 18.5:
  print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
  print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
  print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
  print('Você está na faixa de obesidade.')
else:
  print('Você está na faixa de obesidade mórbida.')
