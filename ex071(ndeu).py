print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
total = valor = int(input('Que valor você quer sacar? R$'))
ced = 50
totced = 0
while True:
    while total >= ced:
        total -= ced
        totced += 1
    print(f'Total de {totced} cédulas de R${ced}')
    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
    totced = 0
    if total == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
