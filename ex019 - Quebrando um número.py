import math
# quando importa informações de uma bibliotéca também posso importar como from math import floor. e então basta usar somente floor
n = float(input("insira um número real: "))
r = math.floor(n)
print("o número real {} em número inteiro é {}".format(n, int(n)))
print("O número real {} em Número inteiro é {}".format(n, r))
