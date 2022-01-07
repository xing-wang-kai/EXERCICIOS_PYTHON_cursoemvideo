import datetime

c = 0
cont = 0
rout = 0
for c in range(1, 8):
    nome = str(input("Qual é seu nome: "))
    ano = int(input("Em qual ano você nasceu: "))
    idade = (datetime.date.today().year) - ano
    print(f"olá {nome} sua idade é de {idade}")
    if idade >= 18:
        print(f"\033[1:33mPARABENS\033[m \033[1:37m{nome}\033[m você alcançou a maior idade")
        cont += 1
    else:
        print(f"{nome} você ainda é menor de idade não tem permissão para o acesso.")
        rout += 1
print("O programa terminou!!")
print(f" o total de pessoas maior de idade é de {cont} \n o total de pessoas menores de idade é de {rout}")