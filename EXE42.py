# CÓDIGO QUE RECEBE 3 SEGMENTOS DO USUÁRIO E CALCULA SE OS 3 PODEM FORMAR UM TRIÂNGULO, RETORNANDO TAMBÉM
# O TIPO DE TRIÂNGULO QUE É FORMADO

seg1 = int(input('Digite o primeiro número: '))
seg2 = int(input('Digite o segundo número: '))
seg3 = int(input('Digite o terceiro número: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('Podem formar um triângulo!')
    if seg1 == seg2 == seg3:
      print('Os 3 segmentos formam um triângilo equilátero!')
    elif seg1 != seg2 != seg3 != seg1:
      print('Os 3 segmentos formam um triângulo escaleno!')
    else:
      print('Os 3 segmentos formam um triângulo isósceles!')
else:
    print('Não formam triângulo.')
