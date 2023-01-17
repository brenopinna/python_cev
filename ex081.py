valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    op = input('Quer continuar? [S/N] ').lower().strip()
    if op == 'n':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
