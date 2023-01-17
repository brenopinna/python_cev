extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = int(input('\nDigite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'\nVocê digitou o número {extenso[num]}.')
        op = input('Deseja continuar?[S/N] ').lower().strip()
    else:
        print('\nTente novamente.', end=' ')
        continue
    if op == 's':
        continue
    else:
        break
