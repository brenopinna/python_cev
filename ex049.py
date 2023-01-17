numero = int(input('Digite o número a ser usado na tabuada: '))
for fator in range (1,11):
    print('{} x {:2} = {}'.format(numero, fator, numero * fator))
