from datetime import datetime
nome = input('Nome: ')
nascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
pessoa = {'nome': nome, 'idade': datetime.now().year - nascimento, 'ctps': ctps}
if ctps != 0:
    contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    pessoa['contratação'] = contratacao
    pessoa['salário'] = salario
    pessoa['aposentadoria'] = contratacao - nascimento + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
