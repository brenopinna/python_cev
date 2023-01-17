d = int(input('\033[34mQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = d*60 + 0.15*km
print('\033[32mO total a pagar é de \033[36mR${:.2f}'.format(preco))