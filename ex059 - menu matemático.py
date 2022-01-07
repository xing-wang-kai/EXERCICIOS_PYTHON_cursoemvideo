opção = 0
while opção != 4:
    print("escolha uma das opções abaixo: \n[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] sair do programa")
    opção = int(input("Qual opção você deseja: "))
    if opção == 1:
        cont = 1
        sair = str(0)
        soma = 0
        while sair not in "Nn":
            cont += 1
            número = int(input(f"Insira o {cont}º número para o soma: "))
            soma += número
            sair = str(input("deseja continuar a somar? [S/N]: ")).upper().upper()
        print(f"o total da soma dos números é de {soma}")
    elif opção == 2:
        cont = 1
        sair = str(0)
        multiplicar = 1
        while sair not in "Nn":
            número = int(input(f"Insira o {cont}º número para a multiplicação: "))
            multiplicar = multiplicar * número
            sair = str(input("deseja continuar a multiplicação: [S/N]: ")).upper()
        print(f"o total da sua multiplicação é de {multiplicar}")
    elif opção == 3:
        cont = 1
        sair = str(0)
        maior = 0
        while sair not in "Nn":
            número = int(input(f"insira o {cont}º para a comparação: "))
            sair = str(input("deseja continuar com a comparação: [S/N]: ")).upper()
            if número > maior:
                maior = número
        print(f"o maior número inserido foi {maior}")
    elif opção == 4:
        print("FIM DO PROGRAMA")
    else:
        print("Opção inválida digite novamente")




