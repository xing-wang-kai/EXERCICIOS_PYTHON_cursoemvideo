import random

lista = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), )

maior = lista[0]
menor = lista[0]
for c, i in enumerate(lista):
    print(f" {i}", end=" ")
    if lista[c] >= maior:
        maior = lista[c]
    if lista[c] <= menor:
        menor = lista[c]
print(f"\n a lista sorteada foi {lista}")
print(f"o número maior é {maior}")
print(f"o número menor e {menor}")

print(f"o maior valor sorteado foi {max(lista)}")
print(f"o menor valor sorteado foi {min(lista)}")