pessoas = []
pessoa = []
pesos = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    pesos.append(peso)
    pessoas.append(pessoa[:])
    pessoa.clear()
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break
maior = max(pesos)
menor = min(pesos)
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
