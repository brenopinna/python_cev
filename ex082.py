valores = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    op = input('Quer continuar? [S/N] ')
    if op[0] in 'nN':
        break
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
