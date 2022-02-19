# CÓDIGO QUE RECEBE DO USUÁRIOS VÁRIOS NOMES E PREÇOS DE PRODUTOS. O USUÁRIO DECIDE QUANDO PARAR DE DIGITAR
# AO FINAL, O TOTAL DOS PREÇOS DEVE SER MOSTRADO, JUNTAMENTE COM A QUANTIDADE DE PRODUTOS QUE CUSTARAM MAIS DE 1000 REAIS
# E O NOME DO PRODUTO MAIS BARATO

totalPreco = 0
nomeMaisBarato = ' '
contM1000 = 0
cont = 1
while True:
    nomeProd = str(input('Digite o nome do produto: '))
    preco = -1
    while preco < 0:
        preco = float(input('Digite o preço do produto: '))
    totalPreco += preco
    if preco > 1000:
        contM1000+=1
    if cont == 1:
        maisBarato = preco
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeMaisBarato = nomeProd
    cont+=1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar digitado (S/N)? ')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'A compra totalizou R$ {totalPreco}.')
print(f'A quantidade de produtos com valor acima de R$ 1000,00 foi {contM1000}.')
print(f'O nome do produto mais barato é {nomeMaisBarato}.')