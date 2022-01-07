nome = str(input("qual o nome que deseja pesquisar? ")).strip()
letras = nome.split()
cores = {"branco": "\033[0;30;40m",
         "vermelho" : "\033[0;31;40m",
         "verde" : "\033[0;32;40m",
         "amarelo": "\033[0;33;40m",
         "azul":"\033[0;34;40m",
         "roxo":"\033[0;35;40m",
         "turquesa": "\033[0;36;40m",
         "cinza": "\033[0;37;40m",
         "fechar": "\033[m",
        }

print("O seu primeiro nome é {} {} {}".format(cores["vermelho"], letras[0], cores["fechar"]))
print("O seu ultimo nome é {}".format(letras[len(letras) - 1]))
