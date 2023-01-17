while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for fator in range(1, 11):
        print(f'{num} x {fator:2} = {num * fator}')
    print('-' * 30)
