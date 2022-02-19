# CÓDIGO QUE RECEBE DO USUÁRIO UM NÚMERO INTEIRO, ENTRE 0 E 20, E RETORNA SEU NOME POR EXTENSO

numeros = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte']

numero = -1
while numero < 0 or numero > 20:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Você digitou um número fora do intervalo requerido. Digite novamente.')
    else:
        print(f'Você digitou o número {numero}, o nome deste número por extenso é {numeros[numero]}.')
