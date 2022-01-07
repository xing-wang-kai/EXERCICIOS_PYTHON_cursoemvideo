print(" Forma de pagameto será no [DINHEIRO], [CHEQUE] ou [CARTÃO]? ")
forma = str(input("insira a forma de pagamento: ")).upper()
if forma == "DINHEIRO" or forma == "CHEQUE":
    valor = float(input("insira o valor da compra: "))
    final = (valor - valor * 10 / 100)
    print("O produto é no valor de R${:.2f} e você pagará o total de R${:.2f}".format(valor, final))
elif forma == "CARTÃO":
    valor = float(input("insira o valor da compra: "))
    condição = str(input("o pagamento será [AVISTA] ou [PRAZO]:" )).upper()
    if condição == "AVISTA":
        final = valor - valor*5/100
        print("o pagamento será no cartão à vista o produto de R${} ficará o preço de R${}".format(valor, final ))
    elif condição == "PRAZO":
        parcela = int(input("Em quatas vezes deseja pagar a mercadoria? "))
        if parcela <= 2:
            final = valor
            print("o valor do produto é de R${} você pagará {} parcelas no valor de R${}".format(valor, parcela, final/parcela))
        else:
            final = (valor+(valor*20/100))
            print("o valor do produto é de R${} você pagará em {} parcelas no valor da parcela e de R${}".format(valor, parcela, final/parcela))
    else:
        print("A condição de pagamento inserida não é válida, por gentileza insira conforme o enunciado")
else:
    print("a forma de pagamento não é válida insira o valor conforme o enunciado")
print("O total de sua compra ficará em R${}".format(final))
