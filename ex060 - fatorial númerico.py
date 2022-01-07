número = int(input("insira um número: "))
cont = número-1
print(f"{número}", end="")
while cont != 0:
    print(f" x{cont}", end="")
    número = número * cont
    cont -= 1
print(f"= {número}")

