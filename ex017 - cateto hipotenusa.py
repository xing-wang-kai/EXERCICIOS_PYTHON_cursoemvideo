from math import hypot
Cateto_oposto = float(input("insira o valor do cateto oposto: "))
cateto_adjacente = float(input("insira o valor do cateto adjacente: "))
hi1 = (Cateto_oposto**2 + cateto_adjacente**2)**(1/2)
hi2 = hypot(Cateto_oposto, cateto_adjacente)

print("A hypotenusa dos catetos oposto {} e cateto adjacente {} é {:.2f}".format(Cateto_oposto, cateto_adjacente, hi1))
print("A hypotenusa dos catetos oposto {} e cateto adjacente {} é {:.2f}".format(Cateto_oposto, cateto_adjacente, hi2))