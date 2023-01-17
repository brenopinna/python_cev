n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if max(n1, n2, n3) == min(n1, n2, n3):
    print('Selecione números diferentes!')
else:
    print('O maior número é {}, e o menor é {}'.format(max(n1, n2, n3), min(n1, n2, n3)))
