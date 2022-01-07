num = int(input("insira um número: "))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f"\033[1:33m{c}\033[m", end=" → ")
        tot += 1
    else:
        print(f"\033[1:32m{c}\033[m", end=" → ")
print("fim do programa")
if tot == 2:
    print(f"o número {num} foi dividido {tot} vezes esse número é primo.")
else:
    print(f"o número {num} foi dividido {tot} vezes esse número não é primo.")