print("-"*40)
print("TABELA DE PREÇOS")
print("-"*40)

listagem = ("Lápis", 1.75,
            "borracha", 2,
            "caderno, ", 15.90,
            "estojo", 2.5,
            "Transferidor", 4.20,
            "compasso", 9.90,
            "mochila", 120.32,
            "canetas", 22.30,
            "livros", 34.90
            )
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>8.2f}")
print("-"*40)