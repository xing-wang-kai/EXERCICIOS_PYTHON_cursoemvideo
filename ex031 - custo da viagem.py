viagem = float(input("digite a distancia de sua viagem em km"))

if viagem >= 200:
    print("Sua viagem será de {}KM o valor de sua viagem será de R${:.2f}".format(viagem, viagem*0.45))
else:
    print("sua viagem será de {}km o valor de sua viagem será de R${:.2f}".format(viagem, viagem*0.50))