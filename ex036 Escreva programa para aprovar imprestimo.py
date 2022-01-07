casa = float(input("Qual o valor da casa pretendida? "))
salário = float(input("Quao o valor do salário atual? "))
qtd_anos = int(input("Quantos anos você vai parcelar a casa? "))

parcelamento = casa/(qtd_anos*12)
sal_aprov = salário*30/100

if parcelamento >= sal_aprov:
    print("seu salário é de {} o parcelamento do imóvel será de R${:.2f} mensais o parcelamento foi negado".format(salário, parcelamento))
else:
    print("seu salário é de R${} o parcelamento do imóvel será de R${:.2f} mensais o parcelamento foi aprovado".format(salário, parcelamento))