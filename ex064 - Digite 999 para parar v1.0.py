condicao = 0
x = soma = 0
condicao = int(input("digite [999] para parar ou um número para soma: "))
while condicao < 999:
    x += 1
    soma += condicao
    condicao = int(input("digite [999] para parar ou um número para soma: "))
print(f"você digiou {x} vezes e a soma de todos números é {soma}")

