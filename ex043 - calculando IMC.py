peso = float(input("Insira o seu peso: "))
altura = float(input("insira a sua altura: "))
IMC = peso/(altura**2)


if IMC <= 18.5:
    print("seu IMC é de {:.2f}kg/m² e você está abaixo do peso ".format(IMC))
elif IMC <= 25:
    print(" o seu IMC é de {:.2f}kg/m² você está no peso ideal".format(IMC))
elif IMC <= 30:
    print(" o seu IMC é de {:.2f}kg/m² você está com sobre peso".format(IMC))
elif IMC <= 40:
    print("o seu IMC é de {:.2f}kg/m² você está obeso".format(IMC))
elif IMC > 40:
    print("o seu IMC é de {:.2f}kg/m² você está obesidade Morbida".format(IMC))