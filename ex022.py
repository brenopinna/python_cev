n_comp = input(('Digite seu nome completo: ').title()).strip()
espacos = int(n_comp.count(' '))
tamanho = int(len(n_comp))
letras = tamanho - espacos
nomes = n_comp.split()
print(f'Nome maiúsculo: {n_comp.upper()}')
print(f'Nome minusculo: {n_comp.lower()}')
print(f'O número de letras, sem espaços: {letras}')
print(f'O número de letras do primeiro nome: {len(nomes[0])}')



