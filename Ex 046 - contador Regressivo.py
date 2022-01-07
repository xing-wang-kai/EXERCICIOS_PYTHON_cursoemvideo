from time import sleep

contagem = int(input("insira um valor inteiro para iniciar a contagem do programa: "))
c = 0
for c in range(contagem, 0, -2):
    print(c)
    sleep(0.25)
print("parabens a contagem finalizou")