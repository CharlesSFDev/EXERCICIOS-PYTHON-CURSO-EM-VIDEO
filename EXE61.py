# CÓDIGO QUE RECEBE DO USUÁRIO O PRIMEIRO TERMO DE UMA PROGRESSÃO ARITMÉTICA, JUNTAMENTE COM SUA RAZÃO DE PROGRESSÃO
# E RETORNA OS 10 PRIMEIROS TERMOS DESTA PROGRESSÃO

primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão de progressão: '))

termos = 0

print('Mostrando os 10 primeiros termos da progressão aritmética: \n')
while termos < 10:
    print(primeiro+(razao)*termos, end = ' ')
    termos+=1