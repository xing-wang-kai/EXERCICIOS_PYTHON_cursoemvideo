from time import sleep
numero = int(input("insira um número para saber a tabuada: "))


for c in range(1, 11):

    calculo = numero * c
    print(f"{numero} x {c} = {calculo}")
    c = c + 1
    sleep(0.30)