salário = float(input("Qual o valor do salário do funcionário: "))
Aumento = float(input("qual a porcentagem do aumento salária?: "))
total = salário * Aumento / 100
valor_final = total + salário

print("Atualmente o valor do salário do funcionário é de R${} \nO aumento recebido pelo funcionário será de R${}\nQue é equivalente a {}%\nO total do novo salário será de R${}".format(salário, total, Aumento, valor_final))