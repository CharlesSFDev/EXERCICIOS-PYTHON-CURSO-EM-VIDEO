# CÓDIGO QUE RECEBE DO USUÁRIO O PRIMEIRO TERMO DE UMA P.A. E SUA RAZÃO DE PROGRESSÃO
# O CÓDIGO PERGUNTA AO USUÁRIO SE ELE QUER CONTINUAR VENDO OS TERMOS DA P.A.

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão de progressão da P.A.: '))

termos = 0

resp = False
print('*'*21)
print('PROGRESSÃO ARITMÉTICA')
print('*'*21)



while not resp:
    if termos < 10:
        print(primeiro + (razao * termos), end=' ')
        termos += 1
    else:
        entrada = int(input('\nDeseja continuar vendo os termos da P.A. Se sim, quantos termos mais você deseja ver? (ou digite 0 para sair) '))
        if entrada != 0:
            for i in range(termos,termos+entrada):
                print('{}º termo: {}'.format((termos+1),(primeiro+(razao*termos)), end = ' '))
                termos+=1
        elif entrada == 0:
            resp = True
print('PROGRAMA FINALIZADO! Ao todo, {} termos da P.A. foram mostrados.'.format(termos))
