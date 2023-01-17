x = int(input('\033[36mDigite um número:\033[m '))
d = 2*x
t = 3*x
r = round(x ** 0.5, 2)
print('Seu dobro é \033[33m{}\033[m, seu triplo é \033[33m{}\033[m e sua raiz quadrada é \033[33m{}\033[m.'.format(d, t, r))
