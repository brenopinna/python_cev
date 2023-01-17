salario = float(input('Digite seu salário: '))
if salario > 1250:
    print('O novo salário é de {:.2f}'.format(salario * 1.1))
else:
    print('O novo salário é de {:.2f}'.format(salario * 1.15))