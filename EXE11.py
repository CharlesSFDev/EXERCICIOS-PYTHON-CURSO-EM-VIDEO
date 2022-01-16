#CÓDIGO QUE RECEBE OS VALORES PARA CALCULAR A ÁREA DE UMA PAREDE E CALCULA A QUANTIDADE, EM LITROS, DE TINTA PARA PINTÁ-LA

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura*largura

print('Para pintar uma parede de {} m2 de área, precisam-se de {} litros de tinta.'.format(area,(area/2)))