import datetime

sexo = str(input("Diga seu sexo, masculino ou feminino? "))

if sexo == "masculino":
    nascimento = int(input("Qual o ano você nasceu: "))
    date_atual = datetime.date.today().year
    calc_data = date_atual - nascimento
    print("{}".format(calc_data))

    if calc_data > 18:
        print("Você já passou dos 18 anos a {} anos você deveria ter se alistado no exercito atualmente você tem {} anos".format(calc_data-18, calc_data))
        ano = date_atual - (calc_data - 18)
        print("você deveria ter se alistado no ano de {} ".format(ano))
    elif calc_data < 18:
        print("Você ainda não tem 18 anos falta ainda {} anos para se alistar no exercito, sua idade é de {} anos".format(18-calc_data, calc_data))
        ano = date_atual + (18 - calc_data)
        print(" Seu alistamento será em {}".format(ano))
    else:
        print("você tem 18 anos, Aliste-se no Exercito")
else:
    print("você não precisa se alistar no exercito!! obrigado")