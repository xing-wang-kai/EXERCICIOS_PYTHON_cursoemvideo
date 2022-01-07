"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. """

import datetime

x = y = z = 0
while True:
    continuar = sexo = " "
    print("-" * 30)
    idade = int(input("qual ano nasceu?: "))
    while sexo not in "FfMn":
        sexo = str(input("Sexo [F/M]: ")).upper().strip()[0]
    print("-"*30)
    data = datetime.date.today().year - idade
    if data > 18:
        x += 1
    elif sexo in "Ff" and idade >= 20:
        y += 1
    elif sexo in "Mm":
        z += 1
    while continuar not in "SsNn":
        continuar = str(input("deseja continuar [S/N]")).upper().strip()[0]
    if continuar in "nN":
        break


print (f"O tatal de pessoas maiores de 18 anos é {x}")
print (f"O total de pessoas mulheres menores de 20 anos é: {y}")
print (f"O total de homens é de : {z}")

