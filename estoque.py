#Criação do dicionário estoque
estoque = {
    "camisa": 50,
    "calça": 15,
    "boné": 35,
    "tenis naique": 35,
}
#Mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")
#Pedindo dados para o usuário do sistema
nome_produto = input("\nInforme o nome do produto vendido: ")
quantidade_vendida = int(input("\nInforme a quantidade vendida: "))
#Atualizar estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("Venda realizada com sucesso!")
else:
    print("Produto não encontrado")
#Mostrar estoque atualizado
for produto, quantidade in estoque.items():
    print(f"{produto} | {quantidade}")