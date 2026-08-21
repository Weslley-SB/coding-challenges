opcao = int(input("Digite (1) para ver a frase da manhã, (2) para a tarde e (3) para noite: "))
match opcao:
    case 1:
        print("Ao vê-la acordar, vejo em seus olhos o mundo refletido pelo brilho de seu olhar")
    case 2:
        escolha = int(input("Digite o se quer a bonita ou a encantadora: (1 ou 2)"))
        if escolha == 1:
            print("O sol arde, arde como olhar;\nO Sol brilha, brilha como seu sorriso")
        elif escolha == 2:
            print("A tarde com você parece infinita, assim como meu amor por você")
        else:
            print("Tudo bem, você não escolheu nenhuma, fica para a proxima.")
    case 3:
        print("Sobre a luz da lua, você é a mais radiante.")