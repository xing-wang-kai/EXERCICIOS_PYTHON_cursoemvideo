import random
v = 0
while True:
    nun = int(input("Digite um número para par ou ímpar: "))
    comp_nun = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    choise = random.choice(comp_nun)
    escolha = " "
    while escolha not in "PpIi":
        escolha = str(input("escolha [P/I]: ")).strip().upper()[0]
    print (f"O computador escolheu {choise}")
    total = nun + choise

    if escolha == "P" and total % 2 == 1:
        break
    elif escolha == "I" and total % 2 == 0:
        break
    else:
        if escolha == "P":
            print(f" você escolheu PAR o total foi {total} você ganhou \033[1:31:40m parabens!!!!\033[m")
        elif escolha == "I":
            print(f" você escolheu IMPAR o total foi {total} você ganhou \033[1:31:40m parabens!!!!\033[m")
    v += 1
print(f"A soma total foi {total} fim de jogo você perdeu")
print(f"Você venceu {v}")



