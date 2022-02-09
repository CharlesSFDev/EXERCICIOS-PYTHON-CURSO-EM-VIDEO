# CÓDIGO QUE RECEBE DO USUÁRIO UMA FRASE E VERIFICA SE A MESMA É UM PALÍNDROMO

frase = str(input('Digite uma frase para verificar se a mesma é um palíndromo: ')).strip().upper() # ELIMINA OS ESPAÇOS ANTES E DEPOIS E COLOCA TUDO EM MAIÚSCULO
palavras = frase.split()  # SEPARA A FRASE EM UMA LISTA DE SÍLABAS
junto = ''.join(palavras) # JUNTA AS SÍLABAS
inverso = ''

# COMANDO EQUVALENTE AO FOR COMENTADO
inverso = junto[::-1]

'''for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
'''
print('Frase digitada: {}. Frase ao contrário: {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo.')

