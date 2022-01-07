numero = int(input("Insira um número: "))
print("você deseja converter o número para qual opção")
print("[1] digite o número para binário")
print("[2] digite o número para octagonal")
print("[3] digite o número para hexadecimal")
opção = int(input("Insira a opção desejada  "))

if opção == 1:
    print("{} convertido para binário é {}".format(numero, bin(numero)[2:]))
elif opção == 2:
    print("{} convertido para octagonal é {}".format(numero, oct(numero)[2:]))
elif opção == 3:
    print("{} convertido para hexadecimal é {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida ")