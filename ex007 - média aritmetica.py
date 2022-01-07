n1 = float(input("primeira nota do aluno: "))
n2 = float(input("digite a segunda nota do aluno: "))
média = (n1+n2)/2
print("a primeira nota do aluno foi de {} \n A segunda nota do aluno foi {} \n A média deste aluno foi de {}".format(n1, n2, média))
if média >= 7 :
    print("O aluno foi aprovado")
elif média == 5 :
    print("aluno recuperação")
else :
    print("aluno reprovado")