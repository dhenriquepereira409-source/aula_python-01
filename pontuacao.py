#CRIAÇÃO DE DICIONARIO
pontos = {}

#ENTRADA DE DADOS
for i in range(5):
    nome = input("Digite seu nome: ")  #chave
    pontuacao = float(input("Informe os pontos iniciais: "))  #valor
    
    pontos[nome] = pontuacao

#ATUALIZAÇÃO DE PONTOS
nome = input("\nDigite o nome do jogador para adicionar pontos: ")
pontos_adicionados = float(input("Informe os pontos conquistados: "))

#VERIFICAÇÃO E SOMA DE PONTOS
if nome in pontos:
    pontos[nome] = pontos[nome] + pontos_adicionados
    print("Pontos adicionados com sucesso!")
else:
    print("Jogador não encontrado.")

#TABELA ATUALIZADA
print("\nTabela de Pontos Atualizada:")
for jogador, pontuacao in pontos.items():
    print(f"{jogador} | {pontuacao}")