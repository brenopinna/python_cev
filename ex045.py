from random import choice
print('\033[31m=\033[m'* 24)
print('\033[36m{:^24}\033[m'.format('JOKENPÔ!!!'))
print('\033[31m=\033[m'* 24)
jokenpo = ['pedra', 'papel', 'tesoura']
pc = choice(jokenpo)
user = str(input('Pedra, papel ou tesoura? ')).lower()
if user == pc:
    print(f'\033[32mEMPATE!\033[m O computador escolheu {pc}')
elif (user == 'papel' and pc == 'tesoura') or (user == 'pedra' and pc == 'papel') or (user == 'tesoura' and pc == 'pedra'):
    print(f'\033[31mUSUÁRIO PERDEU!!!\033[m O computador escolheu {pc}')
elif (user == 'papel' and pc == 'pedra') or (user == 'pedra' and pc == 'tesoura') or (user == 'tesoura' and pc == 'papel'):
    print(f'\033[36mUSUÁRIO VENCEU!!!\033[m O computador escolheu {pc}')
