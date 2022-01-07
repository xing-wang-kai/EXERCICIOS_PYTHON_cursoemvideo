import math
angulo = float(input("ensira o ângulo para saber os dados: "))
seno = math.sin(math.radians(angulo))
cose = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("o Seno do ângulo {}º é igual á: {:.2f}".format(int(angulo), seno))
print("o conseno do Ângulo {}º é igual á: {:.2f}".format(int(angulo), cose))
print("A tangente do Ângulo {}º é igual á: {:.2f}".format(int(angulo), tan))
