frase = (input('Digite uma frase: ').lower()).strip()
print(f"A letra A aparece {frase.count('a')} vezes nesta frase")
print(f"A letra A aparece pela primeira vez no {int(frase.find('a')) + 1}° caractere")
print(f"A letra A aparece pela última vez no {int(frase.rfind('a')) + 1}° caractere")
