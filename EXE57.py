# CÓDIGO QUE RECEBE DO USUÁRIO UMA OPÇÃO DE SEXO, MAS SÓA ACEITE 'M' OU 'F', E CASO NÃO SEJA, CONTINUE RECEBENDO
# DO USUÁRIO UMA DAS OPÇÕES DESEJADA

entrada = 'G'

while entrada.upper() != 'M' and entrada.upper() != 'F':

    entrada = str(input('Digite o sexo da pessoa (M/F): '))

    if entrada.upper() != 'M' and entrada.upper() != 'F':
        print('Entrada inválida!!')

if entrada.upper() == 'M':
    print('O sexo digitado foi M.'.format(entrada))
elif entrada.upper() == 'F':
    print('O sexo digitado foi F.'.format(entrada))

# RESPOSTA ALTERNATIVA

''' entrada = str(input('Digite o sexo da pessoa (M/F): ')),strip().upper()[0]
    while entrada not in 'MmFf':
        entrada = str(input('Digite o sexo da pessoa (M/F): ')),strip().upper()[0]
    print('Sexo {} registrado com sucesso!'.format(entrada)
    '''