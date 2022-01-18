#CÓDIGO QUE RECEBE DO USUÁRIO O VALOR DE Km RODADOS E DIAS DE ALUGUEL, E CALCULA O VALOR TOTAL DO ALUGUEL DO CARRO

kmRod = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias que ficou com o carro: '))

aluguel = (0.15*kmRod)+(60*dias)

print('Considerando os {} Km rodados em {} dias, você deve pagar o valor de {} reais de aluguel!'.format(kmRod,dias,aluguel))
