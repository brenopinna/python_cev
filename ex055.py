pesos = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso [{c}]: '))
    pesos.append(peso)
pmax = max(pesos)
pmin = min(pesos)
print(f'O maior peso foi de {pmax} kg e o menor foi de {pmin} kg.')
