Produto = 300.00

Metodo = float(input("Qual a forma de pagamento?\n [1] para Dinheiro \n [2] para Cheque \n [3] para Cartão "))

if Metodo == 3:
    parcela = int(input("\nEm quantas vezes você ira parcelar?\n Preços:\n a vista 5% de Desconto\n em 2x, preço normal\n em 3x ou mais, 20% de juros.\n Digite '1' para pagamento a vista\n Sua Resposta: "))

if Metodo == 1 or Metodo == 2:
    desconto = Produto * 0.10
    Produto -= desconto
    print("A compra sera no valor de R$", Produto)

elif Metodo == 3 and parcela < 2:
    desconto = Produto * 0.05
    Produto -= desconto
    print("A compra sera no valor de R$", Produto)

elif Metodo == 3 and parcela == 2:
    print("A compra sera no valor de R$", Produto)
    parcelas = Produto / parcela
    print(f"Com {parcela} parcelas de R$ {parcelas}")

else:
    juros = Produto * 0.20
    Produto += juros
    print("A compra sera no valor de R$", Produto)
    parcelas = Produto / parcela
    print(f"Com {parcela} parcelas de R$ {parcelas}")