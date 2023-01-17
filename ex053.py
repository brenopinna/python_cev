frase = input('Frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
contrario = junto[::-1]
if junto == contrario:
    print(f' A frase "{frase}" \033[32mé um palíndromo')
else:
    print(f' A frase "{frase}" \033[31mnão é um palíndromo')
