#CÓDIGO QUE RECEBE DO USUÁRIO UM NOME DE CIDADE DE VERIFICA SE SEU PRIMEIRO NOME É "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip()

print((cidade[0:5].upper()) == 'SANTO')