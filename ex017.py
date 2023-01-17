from math import sqrt
op = float(input('Insira o comprimento do cateto oposto: '))
adj = float(input('Insira o comprimento do cateto adjacente: '))
hip = sqrt(op*op + adj*adj)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))