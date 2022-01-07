"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente."""

little_list = list()

answer = "S"

while True:
    n = int(input("please input a number in list: "))
    if n not in little_list:
        print(f"The {n} value has been successfully added..")
        little_list.append(n)
    else:
        print("this value has already been added and will not be added again")
    r = str(input("do you want continue?: [S/N] ")).upper().strip()[0]
    if r in "Nn":
        break

little_list.sort()
print(f"the number you had choice is in the list {little_list} This list is sorted")
