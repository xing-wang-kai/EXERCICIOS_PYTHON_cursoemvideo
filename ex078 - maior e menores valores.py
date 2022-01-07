
tuple = []
for c in range(0, 5):
    valor = int(input(f"digite um valor na posição {c}: "))
    tuple.append(valor)
    if c == 0:
        maior = menor = valor
    else:
        if maior < valor:
            maior = valor
        if menor > valor:
            menor = valor

print(f"a lista digitada foi: {tuple}")
print(f" o maior valor digitado foi {maior} na posições: ", end=" ")
for i, v in enumerate(tuple):
    if tuple[i] == maior:
        print(f"{i}...", end="")
print(" ")
print(f" o menor valor digitado foi {menor} na posições: ", end=" ")
for j, w in enumerate(tuple):
    if tuple[j] == menor:
        print(f"{j}...", end="")

