salário = float(input("Insira seu salário: "))

Aumento1 = (salário*15/100) + salário

if salário < 1250 :
    print("o aumento do salário será de 15% atualmente você ganha R${} e passará a ganhar R${}".format(salário, Aumento1))
else:
    print("o aumento do salário será de 10% atualmente você ganha R${} e passará a ganhar R${} ".format(salário, salário + (salário*10/100)))


#if salário < 1250:
#   novo = salário + (salário*15/100)
#else:
#   novo = salário + (salário*10/100)
# print("o seu novo salário será de R${}".format(novo))