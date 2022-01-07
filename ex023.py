nun = int(input("insira um número: "))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10

print("a unidade do número é: {}".format(u))
print("a dezena deste número é: {}".format(d))
print("a centena deste número é: {}".format(c))
print("o milhar deste úmero é: {}".format(m))
