print("-"*40)
print("{:-^50}".format("\033[1:34m BEM VINDO AO MERCADINHO\033[m"))
print("-"*40)
x = total = y = menor = 0
continuar = barato = " "


while True:
    print("-" * 40)
    produto = str(input("digite o nome do produto: "))
    preco = float(input("digite o valor desta mercadoria: "))
    continuar = str(input("Deseja continuar? ")).strip().upper()[0]
    while continuar not in "NnSn":
        continuar = str(input("Deseja continuar? ")).strip().upper()[0]
    print("-"*40)
    y += 1
    if y == 1:
        barato = produto
        menor = preco
    else:
        if preco <= menor:
            barato = produto
    if preco >= 1000:
        x += 1
    total += preco
    if continuar == "N":
        break


print("-"*40)
print(f"O total gasto nesta compra foi de {total}")
print(f"Você comprou {x} produto com valor superior a R$1000,00")
print(f"O menor valor desta compra foi {barato}")
print("{:-^50}".format("\033[1:31m OBRIGADO PELA PREFERENCIA!!!\033[m"))
print("-"*40)

