n1 = int(input("Insira um número: "))
n2 = int(input("insira um número: "))

if n1 > n2:
    print("o valor de {} é maior que {}".format(n1, n2))
elif n1 == n2:
    print("os números {} e {} são iguais".format(n1, n2))
else:
    print("o primeiro número {} é menor que o segundo número {}".format(n1, n2))
