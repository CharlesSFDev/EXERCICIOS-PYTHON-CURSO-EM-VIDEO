# CÓDIGO QUE CALCULA A AUTORIZAÇÃO OU NÃO DE UM FINANCIAMENTO IMOBILIÁRIO

salario = int(input('Digite seu salário: '))

valorCasa = int(input('Digite o valor da casa: '))

anos = int(input('Em quantos anos deseja pagar pela casa? '))

parcelas = anos*12

valorParc = valorCasa/parcelas

print('Com seu salário de R$ {}, para comprar uma casa no valor de R$ {} em {} anos, serão precisas {} parcelas de R$ {} cada.'.format(salario,valorCasa,anos,parcelas,valorParc))

if valorParc <= (salario*0.3):
  print('Seu empréstimo foi aprovado!!')
else:
  print('Seu empréstimo não foi aprovado.')
