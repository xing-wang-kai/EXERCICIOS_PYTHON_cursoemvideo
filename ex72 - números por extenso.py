
resposta = "S"

while resposta in "Ss":
    extenso = ("""zero um dois três quatro cinco seis 
                sete oito nove dez onze doze treze quatorze 
                quinze dezesseis dezessete dezoito dezenove vinte""").split()

    try:

        while True:
            numero = int(input("digite um número de 0 até 20: "))
            if 0 <= numero <= 20:
                break
            print("você não digitou um número entre 0 e 20 digite novamene.")
    except:
        print("ocorreu um erro ao digitar o número")
    else:
        print(f"o número digitado foi {numero} por extenso ele equivale á {extenso[numero]}")
    finally:
        resposta = str(input("deseja continuar?: [S/N]")).upper()
        while resposta not in "SsNn":
            print("você digitiou uma opção inválida digite novament: ")
            resposta = str(input("deseja continuar?: [S/N]")).upper()
print("fim do programa!!!")




