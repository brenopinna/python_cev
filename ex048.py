soma = 0
cont = 0
for numero in range(3, 496, 6):
        soma += numero
        cont += 1
print(f'A soma dos {cont} valores pedidos é \033[34m{soma}')
