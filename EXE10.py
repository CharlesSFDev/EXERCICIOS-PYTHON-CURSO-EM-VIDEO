#CÓDIGO QUE RECEBE DO USUÁRIO O VALOR DE UMA CARTEIRA EM REAIS E CALCULA QUANTO DÓLARES PODEM SER COMPRADOS COM ESTE VALOR

carteira = float(input('Digite o valor, em reais, do seu montante em dinheiro: '))

dolar = 5.53

poder = carteira/dolar

print('Com o valor de {} reais, você pode comprar até {} dólares.'.format(carteira,poder))