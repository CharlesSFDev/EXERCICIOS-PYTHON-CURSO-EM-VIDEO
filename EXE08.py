#CÓDIGO QUE RECEBE DO USUÁRIO UMA MEDIDA EM metros E RETORNA A MESMA MEDIDA EM milímetros E centímetros

metros = float(input('Digite o valor da medida em metros: '))

milimetros = metros*1000
centimetros = metros*100

print('A medida de {} metros equivale a {} centímetros e {} milímetros'.format(metros,centimetros,milimetros))
