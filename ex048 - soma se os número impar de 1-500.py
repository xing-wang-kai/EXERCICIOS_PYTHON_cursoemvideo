
c = 0
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f"o valor total de c é {soma} e foram calculados {cont} vezes")