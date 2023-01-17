casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite o tempo de pagamento, em anos: '))
prestacao = casa / (anos * 12)
print('\033[35mO valor da prestação mensal é de R${:.2f}'.format(prestacao))
if prestacao > salario * 0.3:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[33m O valor da parcela é\nsuperior a 30% do seu salário!')
elif prestacao <= salario * 0.3:
    print('\033[32mEMPRÉSTIMO APROVADO!\033[34m O valor da parcela\né menor ou igual a 30% do seu salário.')
