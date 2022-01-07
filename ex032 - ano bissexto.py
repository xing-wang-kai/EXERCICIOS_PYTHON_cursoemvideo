from datetime import date
ano = int(input("digite o ano que você deseja saber se é ou não bissexto: "))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano informado é bissexto: você informou o ano {}".format(ano))
else:
    print("O ano {} não é bissexto.".format(ano))
print("="*22, "obrigado por usar nosso app", "="*22)

# este aqui foi muito dificil de fazer. anos multiplos de 100 que não sao multiplos de 400