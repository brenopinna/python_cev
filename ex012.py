antigo = float(input('\033[32mInsira o preço do produto: '))
desconto = round((antigo * 0.95),2)
print('\033[31mO novo preço do produto é de \033[34m{} R$.'.format(desconto))