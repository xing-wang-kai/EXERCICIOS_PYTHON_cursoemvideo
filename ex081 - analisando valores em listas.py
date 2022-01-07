"""Exercício Python 081: Crie um programa que vai
ler vários números e colocar em uma lista.
Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista"""

little_list = []

while True:
    n = int(input("please input one value at list: "))
    r = str(input("Do you want continue? [S/N] ")).upper().strip()[0]
    little_list.append(n)
    if r not in "Ss":
        break

total = len(little_list)
little_list.sort(reverse=True)



print(f" the input list is {little_list} the value has reverse sorted, this list have a {total} number" )
if 5 in little_list:
    five = little_list.count(5)
    print(f"found {five} number five in the list")
else:
    print("number five aren't in the list")