num = int(input('Número: '))
divisores = 0
for divisor in range(1, num + 1):
    if num % divisor == 0:
        divisores += 1
        print(f'\033[32m{divisor}\033[m', end= ' ')
    else:
        print(f'\033[31m{divisor}\033[m', end= ' ')
print(f'\nO número {num} foi divisível {divisores} vezes, e por isso ele', end= ' ')
if divisores == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
