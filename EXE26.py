# CÓDIGO QUE RECEBE UMA FRASE DO USUÁRIO E BUSCA DENTRO DELA A LETRA "A", RETORNANDO SUA PRIMEIRA E SUA ÚLTIMA POSIÇÃO

frase = str(input('Digite sua frase: ').upper()).strip()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira aparição da letra A foi na posição: {}.'.format(frase.find('A')+1))
print('A última aparição da letra A foi na posição: {}.'.format(frase.rfind('A')+1))