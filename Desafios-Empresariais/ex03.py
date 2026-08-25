# 1. Classe Chocolate
# Esta classe representará o produto final fabricado.

# Atributos:
# nome (Texto): O nome comercial do chocolate (ex: "Trufa de Morango").
# tipo (Texto): A classificação (ex: "Ao leite", "Amargo", "Branco").
# percentual_cacau (Número): A porcentagem de cacau na receita (ex: 70.5).
# preco_venda (Número): O valor de venda da unidade.
# quantidade_estoque (Inteiro): Inicia sempre em 0.

# Métodos:
# produzir(quantidade): Recebe um número inteiro e adiciona essa quantidade ao atributo quantidade_estoque.
# despachar(quantidade): Subtrai a quantidade do estoque. Deve verificar se há estoque suficiente antes de realizar a operação. Caso não haja, deve exibir uma mensagem de erro.
# exibir_detalhes(): Imprime na tela todas as informações do chocolate.

# 2. Classe Fabrica
# Esta classe gerenciará os produtos que a empresa fabrica.

# Atributos:
# nome_empresa (Texto): Nome da fábrica.
# catalogo (Lista/Array): Uma lista que armazenará os objetos do tipo Chocolate.

# Métodos:
# adicionar_produto(chocolate): Recebe um objeto Chocolate e o adiciona à lista do catálogo.
# listar_estoque(): Percorre o catálogo e chama o método exibir_detalhes() de cada chocolate.
# calcular_valor_total_estoque(): Calcula e retorna a soma do valor financeiro de todo o estoque (quantidade * preço de venda de cada item no catálogo).

# Tarefas de Execução
# Crie as classes com seus respectivos atributos e métodos.
# Instancie (crie) a fábrica "Cacau & Cia".
# Instancie 3 objetos do tipo Chocolate com características diferentes.
# Adicione os 3 chocolates ao catálogo da fábrica.
# Simule a produção: chame o método produzir() para adicionar quantidades diferentes de cada chocolate.
# Simule uma venda: chame o método despachar() para reduzir o estoque de um dos chocolates.
# Teste o erro: tente despachar uma quantidade maior do que a existente em estoque de algum produto.
# Exiba o estoque completo usando listar_estoque().
# Imprima o valor financeiro total armazenado no estoque da fábrica.

class Chocolate():
    def __init__(self, nome, tipo, percentual_cacau, preco_venda, quantidade_estoque):
        self.nome = nome
        self.tipo = tipo
        self.percentual_cacau = percentual_cacau
        self.preco_venda = preco_venda
        self.quantidade_estoque = quantidade_estoque

    def produzir(self, quantidade):
        self.quantidade = quantidade
        return self.quantidade_estoque + quantidade

    def despachar(self, quantidade):
        self.quantidade = quantidade
        return self.quantidade_estoque - quantidade

    def __str__(self):
        return f"O chocolate {self.nome} é do tipo {self.tipo}, e tem {self.percentual_cacau}%, o preço atual é de {self.preco_venda} e possui {self.quantidade_estoque} unidades"



c1 = Chocolate("Nestlé", "Ao leite", "0%", 11.37, 7)


print(c1)