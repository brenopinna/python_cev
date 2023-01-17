#com o while:
fatorial = num = int(input('Digite um número: '))
fator = num
print(f'{num}! = {num}', end=' ')
while fator > 1:
    fator -= 1
    fatorial *= fator
    print(f'x {fator}', end=' ')
print(f'= {fatorial}')

#com o for:
n = int(input('Digite um número: '))
print(f'{n}! = ', end='')
fatorial = 1
for fator in range(n, 0, -1):
    if fator != 1:
        print(f'{fator} x ', end='')
    else:
        print(f'{fator} = ', end='')
    fatorial *= fator
print(fatorial)

