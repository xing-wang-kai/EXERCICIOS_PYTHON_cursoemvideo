prin = int(input("insira o primeiro termo: "))
razao = int(input("insira a razão do termo: "))
decimo = prin + (10 - 1) * razao #retorno o décimo termo da razão informada no sistema

for c in range(prin, decimo + razao, razao):
    print(f"{c}", end="  →")
print("ACABOU!!!")