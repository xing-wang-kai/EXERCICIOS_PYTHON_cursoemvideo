#frase = "curso de python no computador"
#print(len(frase)) - informa a qtd de caracteres em uma string, conta também espaços
#print(frase.count("o")) - localiza número de letras especificadas em uma string e mostra a qtd
#print(frase.find("python")) - localiza e retorna o inicio em uma string como números.
#print(frase.replace("python", "android")) - substituiu palavras em uma fraze, ex sub python para android
#print(frase.upper()) - transforma a fraze em letras maiusculas
#print(frase.lower()) - transforma a fraze em letras minusculas
#print(frase.capitalize()) - transforma a primeira letra da string em maiúscula
#print(frase.title()) - transforma a rimeira letra de toda as palavras em uma string em maiúscula
#print(frase.split()) - divide uma string conforme seu número de palavras
#print(frase.strip()) - remove todos espaços antes e depois da string
#frap = frase.split()
#"--".join(frap)

nome = str(input("digite seu nome: ")).strip()
print("analisando seu nome....")
print("seu nome em letras maiusculas é {}".format(nome).upper())
print("seu nome em letras minusculas é {}".format(nome).lower())
print("seu nome possui: {} letras".format(len(nome) - nome.count(" ")))
serapa = nome.split()
print('seu primeiro nome é {}, e seu primeiro nome tem {} letras'.format(serapa[0], len(serapa[0])))
print("seu nome possui tantas {} letras ".format(nome.find(" ")))
print("seu nome mudou para {}".format(nome.replace("deusnir", "kai")))
print("_".join(serapa))


