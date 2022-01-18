#CÓDIGO QUE RECEBE O VALOR DE UM PRODUTO E CALCULA SEU NOVO VALOR COM 5% DE DESCONTO

valor = float(input('Digite o valor do produto: '))

desconto = 5/100

novoValor = valor - (valor*desconto)

print('O produto com valor de {} reais, com 5% de desconto passa a ser {} reais.'.format(valor,novoValor))