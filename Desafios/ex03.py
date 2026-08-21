lista = []
lado1 = int(input("Digite em cm os lados das retas, a primeira:"))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

valores = lado1, lado2, lado3
lista.extend(valores)
lista = sorted(lista)

calculo = lista[0] + lista[1]
if calculo > lista[2]:
    print(f"A soma do menores lados são {calculo}, e o maior lado é {lista[2]}, assim as retas formam um triangulo")
else: 
    print("Não é possivel formar um triangulo.")

print("\n=== Seu Triangulo é: ===\n")

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("Equilatero")
elif lado1 == lado2 or lado2 == lado3:
    print("Isósceles")
else:
    print("Escaleno")