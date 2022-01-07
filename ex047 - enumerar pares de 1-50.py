from time import sleep

c = 0
for c in range(0, 51, 4):
    print("..", end= ' ')
    print(f"\033[1:31m {c}\033[m", end=" ")
    print("..", end=" ")
    sleep(0.25)

print("o programa finalizou")