# CÓDIGO QUE RECEBE DO USUÁRIO UMA VELOCIDADE EM km/h E CALCULA SE O VEÍCULO SERÁ MULTADO OU NÃO
# CALCULANDO SUA MULTA, CASO A VELOCIDADE SEJA ACIMA DA LIMITE

velocidade = float(input('Digite a velocidade do veículo (em km/h): '))

if velocidade > 80:
    print('Velocidade acima do limite do radar!!')
    multa = (velocidade-80)*7
    print('Multa por excesso de velocidade = R$ {}.'.format(multa))
else:
    print('Velocidade dentro do limite permitido!!')
