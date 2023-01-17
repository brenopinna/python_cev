def leiadinheiro(msg):
    while True:
        preco = input(msg).strip().replace(',', '.').strip()
        if preco.isalpha() or preco == '':
            print(f'\033[1;31mERRO: "{preco}" é um preço inválido!\033[m')
        else:
            return float(preco)
