a = int(input("Digite um valor para o número A:"))
b = int(input("Digite um valor para o número B: "))
c = int(input("Digite um valor para o número C: "))

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c

print("O maior número é o {}".format(maior))
print("O menor número é o {}".format(menor))