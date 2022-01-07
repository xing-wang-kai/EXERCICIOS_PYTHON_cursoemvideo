altura = float(input("Qual a altura de sua parede: "))
largura = float(input("qual é a largura da paede: "))
m2 = float(altura*largura)
tinta = m2 / 2
print("sua parede tem altura: {}m \nsua parede tem largura de: {}m \ne a area da parede é {}m² \nPara pintar sua parede você vai precisar de tantos {}l de tinta".format(altura, largura, m2, tinta))
