qtd = int(input("Insire a quantida de vezes que deseja a sequências: "))
x = 3
t1 = 0
t2 = 1
print(f"{t1} + {t2}", end =" + ")

while x <= qtd:
    t3 = t1 + t2
    print(f"{t3}", end = " + ")
    t1 = t2
    t2 = t3
    x += 1
print("FIM")