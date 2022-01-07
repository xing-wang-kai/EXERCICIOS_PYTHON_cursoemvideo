from time import sleep

print("=-"*15, "VERIFICADOR DE TRIÂNGULOS", "=-"*15)
ang1 = int(input("insira a primeira das aresta do triângulo: "))
ang2 = int(input("insira a segunda das aresta do triângulo: "))
ang3 = int(input("insira a terceira das aresta do triângulo: "))
print("verificando....")
sleep(1.5)
if ang1 + ang2 < ang3 or ang1 + ang3 < ang2 or ang2 + ang3 < ang1:
    print("=-"*40)
    print( "\033[1:31:40m ATENÇÃO \033[m os valores inseridos não formam um triângulo.")
    print("-="*40)
else:
    if ang1 == ang2 == ang3:
        print("\033[1:31:40m=-\033[m"*40)
        print("você apresentou um triângulo do tipo: \033[1:31:40m EQUILÁTERO\033[m")
        print("As três aresta apresentada são inguais")
        print("\033[1:31:40m=-\033[m" * 40)
    elif ang1 == ang2 != ang3 or ang1 == ang3 != ang2 or ang2 == ang3 != ang1:
        print("\033[1:32:40m=-\033[m" * 40)
        print("você apresentou um triângulo do tipo: \033[1:32:40m ISÓSCELES\033[m ")
        print("Duas aresta iguais e uma diferente")
        print("\033[1:32:40m=-\033[m" * 40)
    elif ang1 != ang2 != ang3:
        print("\033[1:33:40m=-\033[m" * 40)
        print("você apresentou um triângulo do tipo: \033[1:33:40m ESCALENO\033[m ")
        print("as três arestas são diferentes")
        print("\033[1:33:40m=-\033[m" * 40)