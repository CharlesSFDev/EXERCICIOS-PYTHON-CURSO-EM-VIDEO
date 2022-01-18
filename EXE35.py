# CÓDIGO QUE RECEBE 3 VALORES DE SEGMENTOS E RETORNA SE OS MESMOS PODEM FORMAR UM TRIANGULO

seg1 = int(input('Digite o primeiro número: '))
seg2 = int(input('Digite o segundo número: '))
seg3 = int(input('Digite o terceiro número: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('Podem formar um triângulo!')
else:
    print('Não formam triângulo.')


