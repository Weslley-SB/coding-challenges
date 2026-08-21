#Programa que explica a categoria do veículo
veiculo = input("Digite se seu veículo é carro, bicicleta, Avião ou Helicóptero: ").lower()
match veiculo:
    case "carro" | "bicicleta":
        print("É veículo Terrestre")
    case "avião" | "Helicóptero":
        print("É veículo áereo")
    case _:
        print("Veículo Desconhecido")