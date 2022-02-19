# CÓDIGO QUE RECEBE DO USUÁRIO DADOS DE IDADE E SEXO DE VÁRIAS PESSOAS. O USUÁRIO DECIDE SE QUER CONTINUAR DIGITANDO
# AO FINAL, O PROGRAMA DEVE DIZER QUANTAS PESSOAS TEM MAIS DE 18 ANOS, QUANTOS HOMENS FORAM CADASTRADOS E QUANTAS MULHERES
# TEM MAIS DE 20 ANOS

cont18 = 0
contH = 0
contM20 = 0
contTotal = 0


while True:
    sexo = ' '
    idade = -1
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()[0]
    while idade < 0:
        idade = int(input('Digite a idade da pessoa: '))
    if (sexo in 'Mm'):
       contH+=1
    if (idade >= 18):
        cont18+=1
    if (sexo in 'Ff') and (idade < 20):
        contM20+=1
    contTotal+=1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar digitando (S/N)? ')).strip().upper()[0]
    if resp.upper() == 'N':
        break

print(f'Você digitou um total de {contTotal} pessoas.')
print(f'Das {contTotal} pessoas cadastradas, {contH} são homens.')
print(f'Das {contTotal} pessoas cadastradas, {cont18} tem mais de 18 anos.')
print(f'Das {contTotal} pessoas cadastradas, {contM20} são mulheres tem menos de 20 anos.')

