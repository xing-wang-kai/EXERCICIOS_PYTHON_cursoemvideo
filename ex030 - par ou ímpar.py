from time import sleep
numero = int(input("digite um número: "))
print("processando...")
sleep(3)
resultado = numero % 2

if resultado == 1:
    print("o número digitado é \033[:33m{}\033[m este número é \033[:31m impar\033[m".format(numero))
else:
    print("o número que você digitou é \033[:33m {}\033[m este número é \033[:32m par\033[m".format(numero))
print("="*21, "OBRIGADO", "="*21)