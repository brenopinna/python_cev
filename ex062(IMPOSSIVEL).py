print('=====================')
print('PROGRESSÃO ARITMÉTICA')
print('=====================\n')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termo = 0
termos = 10
while termo < termos:
    print(f'{a1}', end='')
    print('=> ', end='')
    an = a1 + r
    a1 = an
    termo += 1
    if termo == termos:
        print('PAUSA')
        opcao = int(input('\nQuantos termos a mais você quer ver? '))
        if opcao > 0:
            termo = 0
            termos = opcao
print('\nACABOU!')
