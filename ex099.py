from time import sleep


def maior(* numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.22)
    if len(numeros) != 0:
        maximo = max(numeros)
    else:
        maximo = 0
    print(f'Foram informados {len(numeros)} valores  ao todo.')
    print(f'O maior valor informado foi {maximo}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
