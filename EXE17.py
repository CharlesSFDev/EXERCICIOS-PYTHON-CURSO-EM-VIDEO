#CÓDIGO QUE RECEBE O VALOR DO CATETO OPOSTO, JUNTO COM O CATETO ADJACENTE E CALCULA A HIPOTENUSA
import math

catOpo = float(input('Digite o valor do cateto oposto: '))
catAdj = float(input('Digite o valor do cateto adjacente: '))

hipot = math.sqrt(pow(catOpo,2)+pow(catAdj,2))

print('A hipotenusa equivale a: {}'.format(hipot))