# CÓDIGO QUE RECEBE O VALOR EM kM VIAJADOS E CALCULA O VALOR DA VIAGEM

kmRod = float(input('Digite o valor (em km) percorrido: '))

totalViagem = 0

if kmRod <= 200:
    totalViagem = kmRod*0.5
    print('O valor total da viagem de {}km foi de R$ {}.'.format(kmRod,totalViagem))
else:
    totalViagem = kmRod*0.45
    print('O valor total da viagem de {}km foi de R$ {}.'.format(kmRod,totalViagem))

