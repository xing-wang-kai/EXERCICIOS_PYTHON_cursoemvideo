
sexo = str(input("qual o sexo desejado [F/M]? ")).strip().upper()[0]
while sexo not in "fmFM":
    sexo = str(input("Dados inválidos: informe [F/M]? ")).strip().upper()[0]
if sexo == "M":
    sexo = "MASCULINO"
else:
    sexo = "FEMININO"
print(f"sexo {sexo} registrado com sucesso!!")


