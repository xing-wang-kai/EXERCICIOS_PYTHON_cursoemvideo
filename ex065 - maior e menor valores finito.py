solicitado = maior = soma = x = menor = 0
solicita = "S"

while solicita == "S":
    valor = int(input("insira um valor: "))
    soma += valor
    x += 1
    if x == 1:
        maior = menor = valor
    else:
        if valor >= maior:
            maior = valor
        if valor <= menor:
            menor = valor
    solicita = str(input("Deseja continuar: [S/N]")).upper().strip()[0]


print(f"o menor valor digitado foi {menor} e o maior valor digitado foi {maior}")
print(f"você digitou o número {x} vezes a médias entre eles é de {soma/x:.2f}")