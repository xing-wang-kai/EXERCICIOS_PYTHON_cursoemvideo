import random
from time import sleep

print("="*20, "JOKENPÔ" "="*20)
print("""
Vamos JOGAR JOKENPÔ escolha:
[Pedra]
[papel]
[tesoura]
""")

escolha = str(input("qual sua escolha: ")).upper()
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ...")
sleep(1)
computador = ["PEDRA", "PAPEL", "TESOURA"]
comput_es = random.choice(computador)

if comput_es == escolha:
    print( "você escolheu {} e o computador escolheu {} vocês \033[1:33mEMPATARAM\033[m".format(escolha, comput_es))
elif comput_es == "PAPEL" and escolha == "PEDRA":
    print("você escolheu {} e o computador escolheu {} você \033[1:31mPERDEU!!\033[m tente novamente".format(escolha, comput_es))
elif comput_es == "PEDRA" and escolha == "TESOURA":
    print("vocÊ escolheu {} e o computador escolheu {} vocÊ \033[1:31mPERDEU!!\033[m tente novamente.".formt(escolha, comput_es))
elif comput_es == "TESOURA" and escolha == "PEDRA":
    print("você escolheu {} e o computador escolheu {} vocÊ \033[1:31mPERDEU!!\033[m tente novamente.".format(escolha, comput_es))
elif comput_es == "PEDRA" and escolha == "PAPEL":
    print("\033[1:32mPARABENS!!\033[m você ecolheu {} e o computador escolheu {}, você venceu!!!".format(escolha, comput_es))
elif comput_es == "PAPEL" and escolha == "TESOURA":
    print("\033[1:32mPARABENS!!\033[m você ecolheu {} e o computador escolheu {}, você venceu!!!".format(escolha, comput_es))
elif comput_es == "TESOURA" and escolha == "PEDRA":
    print("\033[1:32mPARABENS!!\033[m você ecolheu {} e o computador escolheu {}, você venceu!!!".format(escolha, comput_es))
else:
    print("escolha uma opção válida para jogor")