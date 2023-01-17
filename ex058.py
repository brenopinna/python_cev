from random import randint

pc = randint(1, 10)
tentativas = 1
chute = int(input('Escolha um número de 1 a 10: '))
while chute != pc:
    if chute < pc:
        print('\033[33mSeu user foi menor que o número secreto!\033[m\n')
    if chute > pc:
        print('\033[34mSeu user foi maior que o número secreto!\033[m\n')
    chute = int(input('Escolha um número de 1 a 10: '))
    tentativas += 1
print(f'\nVocê ACERTOU! O número secreto é \033[32m{chute}\033[m e você precisou de \033[33m{tentativas}'
      f' palpite(s)\033[m para acertá-lo!')
