sexo = input('Sexo [M/F]? ').strip()[0]
while sexo not in 'MmFf' or sexo == '':
    sexo = input('OPÇÃO INVÁLIDA! Digite novamente: ').strip()[0]
print(f'Sexo {sexo.upper()} registrado com sucesso.')
