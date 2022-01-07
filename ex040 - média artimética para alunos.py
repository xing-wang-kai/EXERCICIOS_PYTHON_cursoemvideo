nota1 = float(input("Qual a primeira nota do aluno: "))
nota2 = float(input("Qual a segunda nota do aluno: "))
n_final = (nota1 + nota2)/2

if n_final < 5:
    print("sua média final foi de {} você foi \033[:31m REPROVADO =( \033[m".format(n_final))
elif n_final > 5 and n_final < 6.9:
    print("sua Média final foi de {} você está em \033[0:33m RECUPERAÇÃO \033[m".format(n_final))
else:
    print("sua Média final foi de {} você foi \033[0:32m APROVADO !!!\033[m".format(n_final))