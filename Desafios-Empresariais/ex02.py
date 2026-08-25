valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salario: "))
anos = int(input("Em quantos anos ira pagar? "))

salario30 = salario * 0.30
mes = anos * 12
prestacao = valorCasa / mes

print(f"Para pegar a casa de {valorCasa} em {anos} anos, a prestação sera de R$ {prestacao:.2f}.")

if prestacao >= salario30:
    print("Não podemos realizar o emprestimo")
else:
    print("O emprestimo foi aprovado")