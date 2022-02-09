# CÓDIGO QUE RECEBE DO USUÁRIO 7 ANOS DE NASCIMENTO DE 7 PESSOAS E RETORNA QUANTOS NÃO SÃO MAIORES DE IDADE
# E QUANTOS SÃO MAIORES DE IDADE

maior = 0
menor = 0
for i in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if (2022 - ano) < 21:
        menor += 1
    else:
        maior += 1
print('Quantidade de pessoas maiores de idade {}.\nQuantidade de pessoas menores de idade {}.'.format(maior,menor))