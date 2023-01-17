salario = float(input('\033[34mInsira o salário: '))
novo = round(salario*1.15, 2)
print('\033[31mO salário reajustado é de \033[35m{:.2f}\033[m R$'.format(novo))