frase = str(input("digite uma fraze: ")).strip()

print("a letra a aparece um total de: {}".format(frase.lower().count("a")))
print("Qual a primira posição da letra a na string? {}".format(frase.upper().find("A")+1))
print("qual a ultima letra a apareceu na posição {}:".format(frase.upper().rfind("A")+1))