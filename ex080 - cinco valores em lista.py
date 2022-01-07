"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""

"""little_list = list()

for c in range(0, 5):
    n = int(input(f"please input the {c+1}º value in this the list: "))
    if c == 0 or n > little_list[-1]:
        little_list.append(n)
    else:
        pos = 0
        while pos < len(little_list):
            if n <= little_list[pos]:
                little_list.insert(pos, n)
                break
            pos +=1

print("*"*50)
print(f"the list you have make is {little_list} the values as sorted")
print("*"*50)"""
c = 0
listinha = []
while True:
    n = int(input("insira um número de 0-9 para adicionar a listinha: "))
    while n > 9 or n < 0:
        print("\033[7:31m VALOR INVÁLIDO \033[m insira um valor menor que 9 e maior que 0")
        n = int(input("insira novamente um valor para a listinha: "))
    if c == 0 and n > listinha[-1]:
        listinha.append(n)
    else:
        pos = 0
        while pos < len(listinha):
            if n <= listinha[pos]:
                listinha.insert(pos, n)
                break
            pos += 1

    r = str(input("deseja continuar? \033[1:31m[S/N]\033[m")).upper().strip()[0]
    while r not in "SsNn":
        r = str(input("digite \033[1:31mS\033[m para sim e \033[1:31mN\033[m para não")).upper().strip()[0]
    if r in "Nn":
        break
    c += 1


print(listinha)



