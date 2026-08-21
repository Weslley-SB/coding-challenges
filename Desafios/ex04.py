from datetime import date

anoAtual = date.today().year
print("Vamos ver se voce esta na hora de se alistar no exército")
nascimento = int(input("Qual seu ano de nascimento?"))
idade = anoAtual - nascimento

print(anoAtual)

if idade >= 18:
    alistar = input("Ja se alistou? ").upper()

if idade >= 18 and alistar == "S":
    alistar = True
else:
    alistar = False

if idade < 18:
    print("Ainda vai se alistar")
    prazo = (idade - 18) * -1
    print(f"Devera se alistar daqui {prazo} anos")
elif idade == 18:
    print("Está na hora de alistar")
elif idade > 18 and alistar == False:
    print("Já passou da hora de alistar")
    prazo = (idade - 18)
    print(f"Passou do prazo a {prazo} anos")
else:
    print("Ja alistou")