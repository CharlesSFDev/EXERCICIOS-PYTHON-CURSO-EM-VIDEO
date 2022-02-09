# CÓDIGO QUE RECEBE O NOME, IDADE E O SEXO DE 4 PESSOAS E RETORNA A MÉDIDA DE IDADE DO GRUPO
# O NOME DO HOME MAIS VELHO E QUANTAS MULHERES TEM MENOS DE 20 ANOS

somaIdade = 0
maiorIdade = 0
nomeMaisVelho = ''
contMulheres = 0

for i in range(1,5):
    nome = str(input('Digite o o nome da {}ª  pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo [M/F] da {}ª pessoa: '.format(i)))
    somaIdade += idade
    if idade > maiorIdade and sexo.upper() == 'M':
        maiorIdade = idade
        nomeMaisVelho = nome
    if idade < 20 and sexo.upper() == 'F':
        contMulheres += 1

mediaIdade = float(somaIdade/4)

print('Média de idade das 4 pessoas: {} anos,'.format(mediaIdade))
print('Nome do homem mais velho: {}. {} tem {} anos.'.format(nomeMaisVelho,nomeMaisVelho, maiorIdade))
print('Quantidade de mulheres com menos de 20 anos de idade: {}.'.format(contMulheres))