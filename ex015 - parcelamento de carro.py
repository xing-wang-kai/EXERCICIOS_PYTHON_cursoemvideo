qtd_dias = int(input("quantidades de dias: "))
km = float(input("quantidade de Km rodados: "))
mensalidade = ((km*0.15)+(qtd_dias*60))

print("alugado por dias {}dias, rodando total de {}km, você pagará o aluguel de R${}".format(qtd_dias, km, mensalidade))