from time import sleep

velocidade = float(input("Qual a velocidade você está percorrendo? "))
print("Calculando....")
sleep(3)
if velocidade > 80:
    multa = (velocidade-80) * 7
    print("\033[:31m MULTADO!!\033[m Você ultrapassou o limite de 80km/h deverá pagar a multa de \033[:31mR${:.2f}\033[m".format(multa))
else:
    print("\033[:33m PARABENS!!! \033[m você andou dentro do limite estabelecido")
print("="*20, "FIM DO CONTATADOR", "="*20)