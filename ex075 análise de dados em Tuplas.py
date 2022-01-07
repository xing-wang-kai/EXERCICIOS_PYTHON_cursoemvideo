
nun1 = int(input("digite o primeiro número: "))
nun2 = int(input("digite o segundo número: "))
nun3 = int(input("digite o terceiro número: "))
nun4 = int(input("digite o quarto número: "))

lista = (nun1, nun2, nun3, nun4)
tupla = []

x = 0

for c in range(0, len(lista)):
    if lista[c] == 9:
        x += 1

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        tupla.append(lista[c])


if 3 in lista:
    print(f"o valor 3 aparece na {lista.index(3) + 1}º posição")
else:
    print(f"o número 3 não foi digitado")
if 9 in lista:
    print(f"o valor 9 apareceu {lista.count(9)} vezes na lista")
else:
    print(f"o número 9 não foi digitado")

print(f"você digitou o total {x} vezes o número 9 ")

print(f"os números pares digitados são {tupla}")

