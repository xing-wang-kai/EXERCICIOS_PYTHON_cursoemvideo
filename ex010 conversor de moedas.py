# considerando o dollar 3.27$

carteira = float(input("quanto você tem na sua carteira: "))
dollar = float(3.27)
total = float(carteira / dollar)

print(f"Com total de R$ {carteira:.2f} você pode comprar US$ {total:.2f}")