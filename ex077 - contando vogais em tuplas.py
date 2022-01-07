"""palavras = ("aprender", "programar", "linguagem", "python", "curso",
            "gratis", "estudar", "praticar", "trabalhar", "mercado",
            "programador", "futuro")
for p in palavras:
    print(f"\n Na palavra {p.upper():-<20} temos:", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"{letra:.>7}", end="")
for j, i in enumerate(palavras):
    print(f"\n No indice {j+1} tempos a palavra: {i.upper():=<20} ", end="")
    for y in i:
        if y.lower() in "aeiou0":
            print(f"{y}", end="")"""

palavra = ("aprender", "programar", "linguagem", "python", "curso",
            "gratis", "estudar", "praticar", "trabalhar", "mercado",
            "programador", "futuro")

for c in palavra:
    print(f"\no valor encontrado foi {c.upper():.<20}", end="")
    for letras in c:
        if letras.lower() in "aeiou":
            print(f"{letras:.>7}", end="")

