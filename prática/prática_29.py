salario = float(input('Digite o valor do salário: '))

if salario > 1250.00 :
    aumento = salario * 10 /100
    salario_f = salario + aumento 
    print('O valor do salário é de {}'.format(salario_f))
if salario <= 1250.00:
    aumento = salario * 15 /100
    salario_f = salario + aumento 
    print('O valor do salário é de {}'.format(salario_f))