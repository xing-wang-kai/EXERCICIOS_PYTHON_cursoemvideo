import datetime

ano = int(input("Qual o ano o atleta nasceu? "))
idade = datetime.date.today().year - ano

if idade <= 9:
    print("O atleta tem {} anos e faz parte da categoria \033[1:30:41m MIRIN  \033[m".format(idade))
elif idade <= 14:
    print(" O atleta tem {} anos e faz parte da categoria \033[1:31:40m INFANTIL \033[m".format(idade))
elif idade <= 19:
    print(" O atleta tem {} anos e faz parte da categoria \033[1:32:40m JUNIOR \033[m".format(idade))
elif idade <= 25:
    print("o atleta tem {} anos e faz parte da categoria \033[1:33:40m SENIOR \033[m".format(idade))
elif idade > 25:
    print("o atleta tem {} anos e faz parte da categoria \033[1:34:40m MASTER \033[m".format(idade))