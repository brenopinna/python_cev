def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        else:
            return real


INT = leiaInt('Digite um Inteiro: ')
REAL = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {INT} e o real foi {REAL}')
