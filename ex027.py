nome = input('Digite seu nome: ').title().strip()
spc1 = nome.find(' ')
spc2 = nome.rfind(' ')
primeiro_nome = nome[:spc1]
ultimo_nome = nome[(spc2 + 1):]
print(f'O primeiro nome é {primeiro_nome} e o último nome é {ultimo_nome}')
