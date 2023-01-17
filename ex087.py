matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira = 0
maior = 0
for linha in range(3):
    for coluna in range(3):
        valor = matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if valor % 2 == 0:
            pares += valor
        if coluna == 2:
            terceira += valor
        if linha == 1:
            if maior == 0 or valor >= maior:
                maior = valor
print('-=' * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')

