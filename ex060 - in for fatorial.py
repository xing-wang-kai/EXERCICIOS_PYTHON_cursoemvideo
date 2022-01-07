n = int(input("insira o número para o fatorial: "))
regreso = 1
print(f"{n}!", end="")
for c in range(n-1, 0, -1):
    print(f" {c}", end="")
    print(f" x" if c > 1 else " = ", end="")
    n = n * regreso
    regreso += 1
print (f" = {n}")
