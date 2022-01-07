num = x = total = 0
while True:
    num = int(input("digite 999 para parar ou digite um número: "))
    if num == 999:
        break
    total += num
    x += 1
print(f"a soma dos números digitados é o total de {total} e você digitou o total de {x}")