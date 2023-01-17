from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    num = inicio
    if inicio > fim:  # Se for decrescente
        passo *= -1
        while num >= fim:
            print(num, end=' ', flush=True)
            num += passo
            sleep(0.21)
    elif inicio < fim:  # Se for crescente
        while num <= fim:
            print(num, end=' ', flush=True)  # Esse flush é pra não dar buffer (atraso)
            num += passo
            sleep(0.21)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input(f'{"Início:":<8}'))
f = int(input(f'{"Fim:":<8}'))
p = int(input(f'{"Passo:":<8}'))
contador(i, f, p)
