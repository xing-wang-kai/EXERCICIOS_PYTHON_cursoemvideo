tabuada = int((input("digite o número da tabuada: ")))
x = 1
print("_"*20)
while x <= 10:
    print(" {}  X  {:>2}  =  {}".format(tabuada, x, tabuada * x))
    x = x + 1
print("_"*20)

print(type(tabuada))