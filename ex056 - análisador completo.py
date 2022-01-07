som_idade = 0
maior_idade = 0
nome_maior = 0
velha = 0
cont = 0

for c in range(1, 5):
    nome = str(input(f"Insira o nome da {c}º pessoa: "))
    idade = int(input(f"insira a idade da {c}º pessoa: "))
    print(f"Digite o sexo da {c}º pessoa")
    sexo = int(input("[1] HOMEM e [2] MULHER   Digite:"))
    som_idade = som_idade + idade

    if c == 1:
        maior_idade = idade
        velha = idade
        homem_idade = idade
    if idade > maior_idade and sexo == 1:
        nome_maior = nome
        homem_idade = idade
    if idade > velha and sexo == 2:
        velha = idade
    if idade <= 20:
        cont += 1

print(f"a média da idade dos 4 participante é de {som_idade / 4}")
print(f"o Homem mais velha do grupo é {nome_maior} e ele tem {homem_idade}")
print(f"a mulher mais velha tem {velha}anos")
print(f"são {cont} mulheres com menos de 20 anos")


