frase = str(input("insira a frase que você deseja saber se é ou não palindormo: ")).upper()
stripar = frase.split()
juntar = "".join(stripar)
print(f"{juntar}")
inverso = ""

for letra in range(len(juntar)-1, -1, -1):
    print(juntar[letra], end="")
    final = (juntar[letra])
    inverso += juntar[letra]
if juntar == inverso:
    print("\n\n\nparabens você achou um palindromo")

    ##APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
    #achei muito dificil este exercicio eu preciso revisar ele
