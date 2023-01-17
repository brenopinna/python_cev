h = h = float(input('\033[34mInsira a altura da parede, em metros: '))
l = l = float(input('Insira a largura da parede, em metros: '))
a = round(h*l,2)
t = a/2
print('\033[35mPara pintar a área de \033[36m{} m²\033[35m desta parede, você precisará de \033[31m{}\033[35m L de tinta'.format(a, t))