
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo}  → ", end="")
    cont += 1
    termo += razao
print("FIM")

def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")


imprimir_mensagem("Python", "ADS")
