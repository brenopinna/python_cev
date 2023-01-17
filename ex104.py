def leiaInt():
    print('-' * 20)
    while True:
        num = input('Digite um número: ').strip()
        if num.isalpha() or num == '':
            print('ERRO! Digite um número inteiro válido.')
            continue
        return num


n = leiaInt()
print(f'Você acabou de digitar o número {n}')
