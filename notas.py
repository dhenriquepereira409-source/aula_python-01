import json
import os

arquivo =  "notas.json"

def carregar_notas():
    if os.path.exists(arquivo):
        try:
            with open(arquivo,"r", encoding="utf-8") as f:
                return json.load(f)
        except(json.JSONDecodeError, IOError):
            print("Erro ao Ler Arquivo JSON")
            return[]
    return []

def salvar_notas(notas):
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(notas, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar notas: {e}")

def adicionar_nota():
    titulo = input("Título da nota: ").strip()
    conteudo = input("Conteúdo da nota: ").strip()

    if not titulo or not conteudo:
        print("As Informações precisam ser preenchidas!")
        return

    notas = carregar_notas()

    nova_nota = {
        "titulo" : titulo,
        "conteudo" : conteudo
    }

    notas.append(nova_nota)
    salvar_notas(notas)
    print("Nota Salva com Sucesso!!!")

def listar_notas():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota encontrada! ")
        return
    print("\nLista de Notas")
    for i, nota in enumerate(notas,1):
        titulo = nota.get("titulo", "Sem titulo")
        print(f"{i:2d} - {titulo}")
    print()

def ler_nota():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota Disponivel.")
        return
    listar_notas()
    try:
        indice = int(input("Digite o numero da nota: "))
        if 0 <= indice < len(notas):
            nota = notas[indice - 1]
            print(f"Titulo: {nota["titulo"]}")
            print(nota["conteudo"])
        else:
            print("Nota Invalida!")
    except ValueError:
        print("Digite um numero válido")

def deletar_nota():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota para apagar! ")
        return
    listar_notas()
    try:
        indice = int(input("Informe a nota a ser apagada: "))
        if 1 <= indice <= len(notas):
            nota_removida = notas.pop(indice - 1)
            salvar_notas()
            print(f"Nota '{nota_removida.get('titulo', 'semtitulo')}, removida")
        else:
            print("Nota Inválida!")
    except ValueError:
        print("Digite um numero Válido. ")

def menu():
    while True:
        print("\n=======APP DE NOTAS=======")
        print("1 - Adicionar notas")
        print("2 - Listar Nomes")
        print("3 - Ler Notas")
        print("4 - Excluir notas")
        print("5 - SAIR ")

        opcao = input("Escolha uma opção: ").strip
        match opcao:
            case "1":
                adicionar_nota()
            case "2":
                listar_notas()
            case "3":
                ler_nota()
            case "4":
                deletar_nota()
            case "5":
                print("Saindo... ")
                break
            case _:
                print("Genius...")

if __name__ == "__main__":
    menu()