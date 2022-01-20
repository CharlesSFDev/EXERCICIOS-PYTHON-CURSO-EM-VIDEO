# CÓDIGO QUE RECEBE DO USUÁRIO O VALOR DE UM PRODUTO, PERGUNTA SUA CONDIÇÃO DE PAGAMENTO
# E APLICA DESCONTO OU ACRÉSCIMO A ESTE VALOR, MOSTRANDO TAMBÉM O VALOR DE CADA PARCELA, CASO O USUÁRIO PREFIRA PARCELAR A COMPRA

valor = float(input('Digite o valor do produto: '))

print('Como deseja pagar?')
print('1 - A vista(dinheiro)/Cheque.')
print('2 - A vista(cartão).')
print('3 - parcelado (até 2x).')
print('4 - parcelado (3x ou mais).')
formaPag = int(input('Digite a forma de pagamento: '))
if formaPag == 1:
  novoValor = valor - (valor*0.1)
  print('Nesta opção de pagamento, o produto ficará por R$ {}.'.format(novoValor))
elif formaPag == 2:
  novoValor = valor - (valor*0.05)
  print('Nesta opção de pagamento, o produto ficará por R$ {}.'.format(novoValor))
elif formaPag == 3:
  parcela = valor/2
  print('Nesta opção de pagamento, o produto ficará por R$ {}. Cada parcela será de R$ {}.'.format(valor,parcela))
elif formaPag == 4:
  qtde = int(input('Em quantas parcelas deseja dividir a compra? '))
  if qtde < 3:
      print('Número de parcelas inválido para esta operação.')
  else:
    novoValor = valor + (valor*0.2)
    parcela = novoValor/qtde
    print('Nesta opção de pagamento, o produto ficará por R$ {}. Cada parcela será de R$ {}.'.format(novoValor,parcela))
else:
  print('Opção de pagamento inválida!')
