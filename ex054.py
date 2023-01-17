from datetime import date

hoje = date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if hoje - nascimento < 21:
        menores += 1
    else:
        maiores += 1
print(f'\n{maiores} pessoas já atingiram a maioridade e {menores} pessoas ainda não.')
