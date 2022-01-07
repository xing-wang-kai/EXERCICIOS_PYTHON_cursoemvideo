import random

escolha = int(input("insira um número de um a 10: "))
pc_escolha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteado = random.randint(1,10)
x = 1
while escolha != sorteado:
    if escolha > sorteado:
        escolha = int(input("o número é menor tente novamente: "))
    else:
        escolhar = int(input("o número é maior tente novamente: "))
    x += 1
print(f"você escolheu {x} números para conseguir acertar o número {sorteado}")