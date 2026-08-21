from random import randint

print("=== Jokenpô ===")

escolhaPC = randint(1, 3)

if escolhaPC == 1:
    jogada = "Tesoura"
elif escolhaPC == 2:
    jogada = "Pedra"
else:
    jogada = "Papel"

escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

while True:
    if escolhaSua == 1 and escolhaPC == 3:
        print(f"\nPC: {jogada} x USER: Tesoura")
        print("Você Ganhou\n")
        escolhaPC = randint(1, 3)
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 1 and escolhaPC == 1:
        print(f"\nPC: {jogada} x USER: Tesoura")
        print("Empate\n")
        escolhaPC = randint(1, 3)
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 1 and escolhaPC == 2:
        print(f"\nPC: {jogada} x USER: Tesoura")
        print("Você Perdeu\n")
        escolhaPC = randint(1, 3)
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    
    elif escolhaSua == 2 and escolhaPC == 1:
        print(f"\nPC: {jogada} x USER: Pedra")
        print("Você Ganhou\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 2 and escolhaPC == 2:
        print(f"\nPC: {jogada} x USER: Pedra")
        print("Empate\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 2 and escolhaPC == 3:
        print(f"\nPC: {jogada} x USER: Pedra")
        print("Você Perdeu\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))


    elif escolhaSua == 3 and escolhaPC == 2:
        print(f"\nPC: {jogada} x USER: Papel")
        print("Você Ganhou\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 3 and escolhaPC == 3:
        print(f"\nPC: {jogada} x USER: Papel")
        print("Empate\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    elif escolhaSua == 3 and escolhaPC == 1:
        print(f"\nPC: {jogada} x USER: Papel")
        print("Você Perdeu\n")
        escolhaSua = int(input("Escolha o que quer jogar:\n  [ 1 ] Tesoura\n  [ 2 ] Pedra\n  [ 3 ] Papel. "))

    
    else:
        break