print('=====================')
print('PROGRESSÃO ARITMÉTICA')
print('=====================\n')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for n in range (1,11):
    an = a1 + (n - 1) * r
    print(f'Termo {n}: {an}')
