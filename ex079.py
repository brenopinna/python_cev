valores = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = input('Quer continuar? [S/N] ').strip().lower()
    if op == 'n':
        break
print('-=' * 21)
print(f'Você digitou os valores {sorted(valores)}')
