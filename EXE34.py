# CÓDIGO QUE RECEBE O VALOR DO SALÁRIO DE UM FUNCIONÁRIO E RETORNA SEU NOVO VALOR COM UM AUMENTO
# DEPENDENDO DO VALOR DO SALÁRIO, O NOVO SALÁRIO SERÁ 10% OU 15% A MAIS

salario = int(input('Digite o salário do funcionário: '))

if salario > 1250:
    novoSalario = salario + salario*0.1
    print('O novo salário, com aumento de 10%, é: R$ {}.'.format(novoSalario))
else:
    novoSalario = salario + salario*0.15
    print('O novo salário, com aumento de 15%, é: R$ {}.'.format(novoSalario))
