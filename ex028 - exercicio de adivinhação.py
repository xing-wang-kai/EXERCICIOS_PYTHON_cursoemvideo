import random
print("="*15, "QUE O JOGO COMEÇE", "="*15)
print("Jogo do adivinha, você consegue adivinhar o número sorteado pelo algoritimo?")
numero = int(input("Escreva um número de 1 até 5: "))
lista = [1, 2, 3, 4, 5]
sorteado = random.choice(lista)
#computador = randint(0,5) - define o sorteio da lista de 0 até 5

if numero == sorteado:
    print("o numero sorteado foi \033[0;31m {}\033[m e o número escolhido foi \033[0;31m{}\033[m parabens \033[0;33;40m YOU WIN \033[m".format(sorteado, numero))
else:
    print("a máquina sorteou o número \033[0;31m{}\033[m A máquina sempre será a melhor, \033[0;31;40m YOU LOSE\033[m".format(sorteado))
print("="*18, "FIM DE JOGO", "="*18)