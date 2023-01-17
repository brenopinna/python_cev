exp = input('Digite a expressão: ')
p_e = []
p_d = []
for c in exp:
    if c == '(':
        p_e.append(c)
    elif c == ')':
        p_d.append(c)
if len(p_d) != len(p_e):
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')
