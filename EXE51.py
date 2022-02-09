# CÓDIGO QUE RECEBE DO USUÁRIO UM NÚMERO INICIAL, UMA RAZÃO DE PROGRESSÃO
# E MOSTRA OS 10 PRIMEIROS TERMOS DA SUA PROGRESSÃO ARITMÉTICA

numero = int(input('Digite um número inicial para a PA: '))
razao = int(input('Digite a razão de progressão da PA: '))

print('Progressão aritmética:')

for i in range(0,10,1):
    print(numero+(razao*i), end=' -> ')
print('FIM')