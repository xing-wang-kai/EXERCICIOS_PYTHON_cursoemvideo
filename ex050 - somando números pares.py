valor = 0
soma = 0
cont = 0
for c in range(1, 7):
    valor = int(input("insira um número inteiro: "))
    if valor % 2 == 0:
        soma = soma + valor
        cont += 1
print(f"você informou {cont} número pares e a soma deles é {soma}")