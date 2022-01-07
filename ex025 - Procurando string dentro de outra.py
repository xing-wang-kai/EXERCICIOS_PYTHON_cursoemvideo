nome = str(input("escreva seu nome: ")).strip()
print(nome[::].lower() == "silva")
print("tem silva em seu nome? {}".format("silva"in nome.lower()))