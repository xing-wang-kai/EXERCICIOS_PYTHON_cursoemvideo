# sistema de tabuada usando o combando BREAK para quebrar o código e while.

while True:
    print("=-"*30)
    nun = int(input("digite um número para mostrar a tabuada: "))
    print("=-"*30)
    if nun <= 0:
        break
    for x in range(1, 11):
        print(f"{nun} X {x} = {nun*x}")

    print("=-"*30)
    print("fim da Tabuada")
    print("=-"*30)

