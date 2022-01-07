print("-="*30)
print("ANALISANDO SE PODE SER TRIANGULO")
print("-="*30)

an1 = float(input("insira o número do primeiro ângulo: "))
an2 = float(input("insira o número do segundo ângulo: "))
an3 = float(input("insira o número do terceiro ângulo: "))

if an1 < an2+an3 and an2 < an1+an3 and an3 < an1+an2:
    print("os âgulos mencionados pode formar um triângulo")
else:
    print("os ângulos mencionados não podem forma um triângulo")

#para um triângulo a soma dos dois angulos nao pode ser menor que o valor do terceiro angulo.
