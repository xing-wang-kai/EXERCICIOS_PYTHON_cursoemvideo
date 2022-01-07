valor = float(input("Quanto custa o produto: "))
desconto = float(input("qual o total do desconto: "))
total = valor / 100 * desconto
total2 = valor - total

print("O produto no valor de R${:.2f} tem um desconto de {}% \nVocê pagará somente R${:.2f} e terá o desconto de R${:.2f}".format(valor, int(desconto), total2, total))