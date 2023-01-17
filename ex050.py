soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Número {c}: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi \033[33m{soma}.')
