km = float(input('A distância em km é de: '))
if km > 200:
    print('O preço da viagem é de R${:.2f}'.format(0.45 * km))
else:
    print('O preço da viagem é de R${:.2f}'.format(0.5 * km))
'''Também pode-se usar o if simplificado:
    preço = km * 0.5 if km <= 200 else km * 0.45'''
