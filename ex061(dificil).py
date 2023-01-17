print('=====================')
print('PROGRESSÃO ARITMÉTICA')
print('=====================\n')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termo = 1
while termo <= 10:
    print(f'{a1}', end='')
    an = a1 + r
    a1 = an
    print('=> ', end= '' if termo != 10 else 'ACABOU!')
    termo += 1
