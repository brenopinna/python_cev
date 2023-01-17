x = int(input('\033[35mInsira um valor em metros:\033[m '))
cm = x*100
mm = x*1000
print('\033[1;36m{}\033[m m corresponde a \033[1;36m{}\033[m cm e \033[1;36m{}\033[m mm.'.format(x,cm,mm))