import random

numero = random.randint(1, 5)

escolha = int(input("Adivinhe o número do Computador: "))

if escolha == numero:
    print("Parabens, você acertou!")
else:
    print("Voce Errou!")