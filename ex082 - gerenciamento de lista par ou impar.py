print("-="*38)

print(
    """\033[1:33mExercício Python 082: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.\033[m"""
)
print("-="*38)

total_list = []
even_list = []
odd_list = []

while True:
    n = int(input("enter a value to insert into the list: "))
    total_list.append(n)
    r = str(input("Do you want to continue? \033[1:31m[S/N]\033[m")).upper().strip()[0]
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)
    if r not in "Ss":
        break
print(f"the \033[1:31m total list \033[mis \033[1:31m{total_list}\033[m")
print(f"the \033[1:33mEven number in list\033[m is \033[1:31m{even_list}\033[m")
print(f"the \033[1:32modd number in list\033[m is \033[1:31m{odd_list}\033[m")