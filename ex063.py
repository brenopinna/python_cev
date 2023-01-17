qtd = int(input('Digite a quantidade de elementos da sequência de Fibonacci: '))
cont = 1
menor = 0
maior = 1
while cont <= qtd:
    an = menor + maior
    print(f'{menor}', end=', ')
    menor = maior
    maior = an
    cont += 1
print('ACABOU!')
