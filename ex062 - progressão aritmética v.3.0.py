primeiro = int(input("insira o primeiro termo: "))
razao = int(input("insira a razão"))
soma = primeiro
x = 0
qtd = 10
solicitar = "S"
while solicitar == "S":
    while x <= qtd:
        print(f"{soma}", end="→ ")
        x += 1
        soma += razao
    print("deseja continuar?:")
    solicitar = str(input("Insira [S/N]")).upper()
    if solicitar == "S":
        mais = int(input("quantas vezes você quer repetir a operação: "))
        qtd += mais
    elif solicitar != "S" or solicitar != "N":
        solicitar = str(input("Insira [S/N]")).upper()
print(f"A quantidade de termos repetidos foi de {qtd}")




