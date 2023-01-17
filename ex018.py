from math import sin, cos, tan, radians
angulo = float((input('Digite o ângulo: ')))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print('O seno de {}° é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(angulo, sen, cos, tg))
