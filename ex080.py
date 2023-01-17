valores = []
menor = 0
index = 0
for c in range(0, 5):
    index = 0
    num = int(input('Digite um valor: '))
    if not valores or num > valores[-1]:
        print('Adicionado ao final da lista...')
        valores.append(num)
    elif valores:
        for valor in valores:
            if num >= valor:
                index = valores.index(valor) + 1
        valores.insert(index, num)
        print(f'Adicionado na posição {index} da lista...')
print('-=' * 20)
print(f'Os valores digitados em ordem foram {valores}')

