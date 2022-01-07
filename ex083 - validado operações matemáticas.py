print("-="*38)
print(
    """\033[1:33mExercício Python 083: Crie um programa 
    onde o usuário digite uma expressão qualquer que use 
    parênteses. Seu aplicativo deverá analisar se a 
    expressão passada está com os parênteses abertos e 
    fechados na ordem correta.\033[m"""
)
print("-="*38)

express = input("type a math expression: ").strip()

open_parentheses = express.count("(")
closed_parentheses = express.count(")")

if open_parentheses != closed_parentheses:
    print("the math expression entered is incorrect.")
else:
    print("the math expression entered is correct.")