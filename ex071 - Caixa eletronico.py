"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print("="*40)
print("{:-^50}".format("\033[1:35m BEM VINDO AO CAIXA ELETRÔNICO\033[m"))
print("{:-^50}".format("\033[1:31m ATENÇÃO ESTE CAIXA SÓ TEM CEDULAS \033[m"))
print("{:-^50}".format("\033[1:31m DE R$50 R$20 R$10 e R$1 \033[m"))
print("="*40)

saque = int(input("Quanto você deseja sacar?"))
celula50 = 50
celula20 = 20
celula10 = 10
celula1 = 1
total50 = total20 = total10 = total1 = 0
while True:
    if saque >= celula50:
        total50 = int(saque/celula50)
        saque = saque % celula50
    elif saque >= celula20 and saque <= celula50:
        total20 = int(saque/celula20)
        saque = saque%celula20
    elif saque >= celula10 and saque <=celula20:
        total10 = int(saque/celula10)
        saque = saque%celula10
    elif saque >= celula1 and saque <= celula10:
        total1 = int(saque/celula1)
        saque = saque % celula1
    elif saque == 0:
        break
if total50 != 0:
    print(f"você vai sacar o total de {total50} notas de R$50")
if total20 != 0:
    print(f"você vai sacar o total de {total20} notas de R$20")
if total10 != 0:
    print(f"você vai sacar o total de {total10} notas de R$10")
if total1 != 0:
    print(f"você vai sacar o totla de {total1} notas de R$1")
