
'''maior = 0
menor = 500

for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}º pessoa: "))
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print(f"o maior peso foi {maior:.2f}kg e o menor peso é de {menor}" )'''

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}º pessoa: "))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f"o maior peso foi {maior:.2f}kg e o menor peso é de {menor}" )


## são duas alternativas para resolver o problema