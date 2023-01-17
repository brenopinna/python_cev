n = int(input('numero: '))
u = n // 1 % 10 #essa divisão inteira indica quantas casas pra esquerda eu ando
d = n // 10 % 10 #//1 = 0, //10 = 1, e assim por diante
c = n // 100 % 10#esse resto da divisão indica quantos números irei pegar,
m = n // 1000 % 10#segue o mesmo raciocínio da divisão inteira (só nao funciona no milhar)
print(f'Unidade: {u}\nDezena: {int(d)}\nCentena: {int(c)}\nMilhar: {int(m)}')