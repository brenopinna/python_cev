n1 = float(input('Lado 1: '))
n2 = float(input('Lado 2: '))
n3 = float(input('Lado 3: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Essas retas podem formar um triângulo.')
    if n1 == n2 == n3:
        print('Esse triângulo é \033[32mEQUILÁTERO\033[m')
    elif n1 != n2 != n3 != n1:
        print('Esse triângulo é \033[31mESCALENO\033[m')
    else:
        print('Esse triângulo é \033[33mISÓSCELES\033[m')
else:
    print('Essas retas não podem formar um triângulo!')
